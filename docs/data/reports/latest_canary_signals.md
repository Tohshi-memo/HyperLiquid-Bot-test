# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T11:37:25.967582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0824` n `12`; crypto_alt avg `0.0123` n `229`; crypto_major avg `0.026` n `8`; equity avg `-0.1144` n `91`; fx avg `0.0052` n `6`; index avg `-0.0117` n `25`; metal avg `0.018` n `20`; unknown avg `0.051` n `763`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `-0.1183` n `229`; crypto_major avg `-0.1211` n `8`; equity avg `-0.21` n `91`; fx avg `-0.0081` n `6`; index avg `-0.0684` n `25`; metal avg `0.0345` n `20`; unknown avg `-0.0447` n `763`
- 4h: commodity avg `-0.0578` n `12`; crypto_alt avg `0.2432` n `229`; crypto_major avg `-0.0111` n `8`; equity avg `-0.4647` n `91`; fx avg `-0.1127` n `6`; index avg `-0.108` n `25`; metal avg `0.2014` n `20`; unknown avg `-0.3404` n `757`
- 24h: commodity avg `0.3785` n `12`; crypto_alt avg `0.4313` n `229`; crypto_major avg `-0.4348` n `8`; equity avg `-1.6929` n `90`; fx avg `-0.1405` n `6`; index avg `-0.4389` n `25`; metal avg `-0.2051` n `20`; unknown avg `-0.3644` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
