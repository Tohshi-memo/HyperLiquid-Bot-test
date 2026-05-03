# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T10:15:21.254970+00:00`
- Correlation status: `ready`
- Asset price records: `160`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `7`; crypto_alt avg `0.0208` n `223`; crypto_major avg `-0.0977` n `7`; equity avg `-0.0261` n `42`; fx avg `0.0` n `4`; index avg `0.0` n `9`; metal avg `0.0022` n `7`; unknown avg `-0.0092` n `313`
- 1h: commodity avg `-0.0328` n `7`; crypto_alt avg `0.2113` n `223`; crypto_major avg `-0.0324` n `7`; equity avg `0.021` n `42`; fx avg `0.0021` n `4`; index avg `0.0258` n `9`; metal avg `0.0095` n `7`; unknown avg `-0.1048` n `313`
- 4h: commodity avg `-0.0355` n `7`; crypto_alt avg `0.6911` n `223`; crypto_major avg `0.3878` n `7`; equity avg `-0.2792` n `42`; fx avg `0.0162` n `4`; index avg `-0.0025` n `9`; metal avg `0.121` n `7`; unknown avg `0.1841` n `313`
- 24h: commodity avg `-0.2322` n `7`; crypto_alt avg `1.2308` n `223`; crypto_major avg `-0.0887` n `7`; equity avg `0.2242` n `42`; fx avg `0.1265` n `4`; index avg `0.099` n `9`; metal avg `0.1119` n `7`; unknown avg `0.1693` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4151`, n `156`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `156`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4004`, n `156`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3864`, n `152`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `156`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3813`, n `152`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3717`, n `152`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3644`, n `152`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3383`, n `156`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3316`, n `156`, moderate_sample_signal
