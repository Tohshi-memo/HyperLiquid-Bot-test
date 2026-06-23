# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T06:03:30.334625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.1459` n `228`; crypto_major avg `-0.0751` n `8`; equity avg `-0.2426` n `86`; fx avg `0.0278` n `6`; index avg `-0.0096` n `23`; metal avg `-0.0241` n `20`; unknown avg `-0.0149` n `684`
- 1h: commodity avg `-0.1632` n `12`; crypto_alt avg `-0.4468` n `228`; crypto_major avg `-0.4242` n `8`; equity avg `-0.7846` n `86`; fx avg `0.0224` n `6`; index avg `-0.1146` n `23`; metal avg `-0.137` n `20`; unknown avg `-0.1955` n `676`
- 4h: commodity avg `-0.1222` n `12`; crypto_alt avg `-0.7251` n `228`; crypto_major avg `-0.9156` n `8`; equity avg `-1.6075` n `86`; fx avg `0.0084` n `6`; index avg `-0.3003` n `23`; metal avg `-0.4191` n `20`; unknown avg `0.3186` n `676`
- 24h: commodity avg `-0.5345` n `12`; crypto_alt avg `-1.4203` n `228`; crypto_major avg `-1.458` n `8`; equity avg `-3.7227` n `85`; fx avg `0.0122` n `6`; index avg `-0.6039` n `23`; metal avg `-1.306` n `18`; unknown avg `0.8119` n `647`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
