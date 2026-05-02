# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T19:45:20.436784+00:00`
- Correlation status: `ready`
- Asset price records: `102`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `7`; crypto_alt avg `0.0446` n `223`; crypto_major avg `-0.017` n `7`; equity avg `-0.0286` n `42`; fx avg `-0.0011` n `4`; index avg `0.0069` n `9`; metal avg `0.0009` n `7`; unknown avg `0.2544` n `313`
- 1h: commodity avg `-0.0393` n `7`; crypto_alt avg `0.2644` n `223`; crypto_major avg `0.1129` n `7`; equity avg `0.141` n `42`; fx avg `0.0021` n `4`; index avg `0.0259` n `9`; metal avg `-0.0144` n `7`; unknown avg `0.2488` n `313`
- 4h: commodity avg `-0.1861` n `7`; crypto_alt avg `0.5629` n `223`; crypto_major avg `0.1026` n `7`; equity avg `0.2685` n `42`; fx avg `0.0383` n `4`; index avg `0.0582` n `9`; metal avg `-0.0332` n `7`; unknown avg `0.3625` n `313`
- 24h: commodity avg `-0.024` n `7`; crypto_alt avg `1.6277` n `223`; crypto_major avg `0.2951` n `7`; equity avg `0.8574` n `42`; fx avg `-0.0233` n `4`; index avg `0.0685` n `9`; metal avg `-0.0933` n `7`; unknown avg `0.4538` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5253`, n `94`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5083`, n `98`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5036`, n `94`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4907`, n `98`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4487`, n `94`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4261`, n `94`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4228`, n `94`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4223`, n `98`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4221`, n `94`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4168`, n `94`, moderate_sample_signal
