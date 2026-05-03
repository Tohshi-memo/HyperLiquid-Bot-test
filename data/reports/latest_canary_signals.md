# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T22:30:27.719133+00:00`
- Correlation status: `ready`
- Asset price records: `209`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0579` n `7`; crypto_alt avg `-0.0545` n `223`; crypto_major avg `-0.0646` n `7`; equity avg `-0.011` n `42`; fx avg `0.008` n `4`; index avg `-0.0462` n `9`; metal avg `0.0085` n `7`; unknown avg `-0.0037` n `314`
- 1h: commodity avg `0.2282` n `7`; crypto_alt avg `0.3626` n `223`; crypto_major avg `0.4168` n `7`; equity avg `-0.0189` n `42`; fx avg `-0.0024` n `4`; index avg `-0.0975` n `9`; metal avg `-0.2288` n `7`; unknown avg `0.2795` n `314`
- 4h: commodity avg `-0.1917` n `7`; crypto_alt avg `0.3815` n `223`; crypto_major avg `0.495` n `7`; equity avg `0.1977` n `42`; fx avg `-0.0122` n `4`; index avg `-0.0312` n `9`; metal avg `-0.1457` n `7`; unknown avg `0.2345` n `314`
- 24h: commodity avg `-0.2219` n `7`; crypto_alt avg `0.0571` n `223`; crypto_major avg `0.4978` n `7`; equity avg `0.3022` n `42`; fx avg `-0.0201` n `4`; index avg `0.0236` n `9`; metal avg `0.3754` n `7`; unknown avg `0.2288` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3918`, n `205`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3746`, n `205`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3716`, n `201`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3678`, n `201`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3495`, n `205`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3374`, n `205`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3051`, n `205`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2938`, n `205`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.2857`, n `205`, moderate_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.2351`, n `205`, weak_sample_signal
