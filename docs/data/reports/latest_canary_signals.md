# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T14:52:24.833991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `-0.0382` n `229`; crypto_major avg `0.0982` n `8`; equity avg `0.0029` n `88`; fx avg `0.0089` n `6`; index avg `0.0041` n `25`; metal avg `0.0077` n `20`; unknown avg `0.0174` n `765`
- 1h: commodity avg `0.0152` n `12`; crypto_alt avg `0.1643` n `229`; crypto_major avg `0.4942` n `8`; equity avg `0.0487` n `88`; fx avg `0.0235` n `6`; index avg `0.0056` n `25`; metal avg `0.006` n `20`; unknown avg `0.0318` n `765`
- 4h: commodity avg `-0.0271` n `12`; crypto_alt avg `0.5878` n `229`; crypto_major avg `0.5967` n `8`; equity avg `-0.0811` n `88`; fx avg `0.0462` n `6`; index avg `0.0034` n `25`; metal avg `0.0148` n `20`; unknown avg `-0.0391` n `759`
- 24h: commodity avg `0.0341` n `12`; crypto_alt avg `0.7482` n `229`; crypto_major avg `1.4869` n `8`; equity avg `0.2872` n `88`; fx avg `-0.0301` n `6`; index avg `-0.0158` n `25`; metal avg `0.0019` n `20`; unknown avg `2.1569` n `741`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
