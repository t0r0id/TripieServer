import numpy as np

def status(sol,data):
    x=sol.x
    y=sol.y
    pi=sol.pi
    
    def objective():   # Total Happiness
        f=0
        for i in range(data.DAYS):
            for j in range (1,data.n+1):
                f=f+data.HAPPINESS[j]*y[j,i]
        return f

    def TimeConstraint():  # 
        boolean=True
        for k in range(data.DAYS):
            sum1=0
            for i in range(0,data.n+1):
                sum2=0
                for j in range(1,data.n+2):
                    sum2=sum2+data.TRAVELTIME[i,j]*x[i,j,k]
                sum1=sum1+data.SERVICETIME[i]*y[i,k]+sum2
            boolean=(boolean and (sum1<=data.TMAX))
        if boolean:
            return [boolean,objective()]
        else:
            return [False,7]

    def ContinuityConstraint():
        boolean=True
        for i in range(data.n+2):
            for j in range(data.n+2):
                for k in range (data.DAYS):
                    boolean=(boolean and (pi[i,k]+data.SERVICETIME[i]+data.TRAVELTIME[i,j]-pi[j,k]<=data.M*(1-x[i,j,k])))
        if boolean:
            return TimeConstraint()
        else:
            return [False,6]
            
    def OneVertexConstraint():
        boolean=True
        for i in range(1,data.n+1):
            for k in range(data.DAYS):
                sum1=np.sum(x[0:data.n+1,i,k])
                sum2=np.sum(x[i,1:data.n+2,k])
                boolean=(boolean and ((sum1==sum2) and (sum1==y[i,k])))
        if boolean:
            return ContinuityConstraint()
        else:
            return [False,5]

    def BudgetConstraint():
        boolean=True
        sum1=0
        for k in range(data.DAYS):
            for i in range(1,data.n+1):
                sum1=sum1+data.COST[i]*y[i,k]
        boolean=(boolean and (sum1<=data.BUDGET))
        if boolean:
            return OneVertexConstraint()
        else:
            return [False,4]

    def OnceConstraint():
        boolean=True
        for h in range(1,data.n+1):
            boolean=(boolean and (np.sum(y[h,:])<=1))
        if boolean:
            return BudgetConstraint()
        else:
            return [False,3]

        
    def DaysConstraint():
        sum1=np.sum(x[0,1:data.n+2,:])
        sum2=np.sum(x[0:data.n+1,data.n+1,:])
        if (((sum1==sum2) and (sum1==data.DAYS))):
            return OnceConstraint()
        else:
            return [False,2]

    def CloseTimeConstraint():
        boolean=True
        for k in range(data.DAYS):
            for i in range (data.n+2):
                boolean=(boolean and (pi[i,k]<=data.CLOSETIME[i]))
        if boolean:
            return DaysConstraint()
        else:
            return [False,1]

    
    return (CloseTimeConstraint()) 
    
