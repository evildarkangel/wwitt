
#ifndef __DB_IFACE__H__ 
#define __DB_IFACE__H__ 

class DBIface {
public:
	DBIface(bool bannercrawl) : bannercrawl(bannercrawl) { }
	virtual ~DBIface() {}

	virtual bool next(std::vector <std::string> & resultset) = 0;

	virtual void updateService(uint32_t ip, unsigned short port, std::string data) = 0;
	virtual void updateVhost(const std::string &vhost, const std::string &url,
	                         std::string data, int flag) = 0;

protected:
	bool bannercrawl;
};


#endif

