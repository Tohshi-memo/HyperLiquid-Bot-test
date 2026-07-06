# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T08:52:31.360850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0634` n `12`; crypto_alt avg `0.0404` n `229`; crypto_major avg `0.0847` n `8`; equity avg `0.09` n `88`; fx avg `-0.0084` n `6`; index avg `0.014` n `25`; metal avg `0.0223` n `20`; unknown avg `-0.0335` n `765`
- 1h: commodity avg `0.1808` n `12`; crypto_alt avg `-0.3874` n `229`; crypto_major avg `-0.3754` n `8`; equity avg `0.0285` n `88`; fx avg `0.004` n `6`; index avg `-0.006` n `25`; metal avg `-0.164` n `20`; unknown avg `-0.0687` n `765`
- 4h: commodity avg `0.1076` n `12`; crypto_alt avg `-0.8365` n `229`; crypto_major avg `-0.7957` n `8`; equity avg `0.0708` n `88`; fx avg `0.0364` n `6`; index avg `0.0533` n `25`; metal avg `0.0628` n `20`; unknown avg `-0.2122` n `731`
- 24h: commodity avg `-0.1399` n `12`; crypto_alt avg `-0.3949` n `229`; crypto_major avg `0.4456` n `8`; equity avg `-0.627` n `88`; fx avg `0.0822` n `6`; index avg `-0.0106` n `25`; metal avg `-0.1913` n `20`; unknown avg `1.0669` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
