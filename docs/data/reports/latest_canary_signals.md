# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T19:30:29.811097+00:00`
- Correlation status: `ready`
- Asset price records: `101`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `7`; crypto_alt avg `-0.0126` n `223`; crypto_major avg `-0.0861` n `7`; equity avg `0.0125` n `42`; fx avg `0.0021` n `4`; index avg `0.0054` n `9`; metal avg `0.0096` n `7`; unknown avg `0.1294` n `313`
- 1h: commodity avg `-0.022` n `7`; crypto_alt avg `0.135` n `223`; crypto_major avg `0.0214` n `7`; equity avg `0.0576` n `42`; fx avg `0.0` n `4`; index avg `0.0216` n `9`; metal avg `-0.0024` n `7`; unknown avg `0.1691` n `313`
- 4h: commodity avg `-0.1775` n `7`; crypto_alt avg `0.5198` n `223`; crypto_major avg `0.1004` n `7`; equity avg `0.2731` n `42`; fx avg `0.0466` n `4`; index avg `0.0604` n `9`; metal avg `-0.0383` n `7`; unknown avg `0.2612` n `313`
- 24h: commodity avg `0.0113` n `7`; crypto_alt avg `1.4283` n `223`; crypto_major avg `0.215` n `7`; equity avg `0.8085` n `42`; fx avg `-0.0287` n `4`; index avg `0.1048` n `9`; metal avg `-0.2806` n `7`; unknown avg `0.572` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5252`, n `93`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5104`, n `97`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4926`, n `97`, moderate_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4923`, n `93`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4499`, n `93`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4302`, n `93`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4252`, n `97`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4247`, n `93`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4215`, n `93`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4191`, n `93`, moderate_sample_signal
