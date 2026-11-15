# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T19:37:28.054760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `13`; crypto_alt avg `-0.2326` n `239`; crypto_major avg `-0.025` n `8`; equity avg `-0.0382` n `162`; fx avg `0.001` n `6`; index avg `-0.0025` n `27`; metal avg `0.0148` n `20`; unknown avg `-0.0566` n `1265`
- 1h: commodity avg `0.0715` n `13`; crypto_alt avg `0.3909` n `239`; crypto_major avg `0.5999` n `8`; equity avg `0.3981` n `162`; fx avg `-0.0028` n `6`; index avg `0.0528` n `27`; metal avg `0.027` n `20`; unknown avg `2.7688` n `1259`
- 4h: commodity avg `0.0587` n `13`; crypto_alt avg `0.0984` n `239`; crypto_major avg `0.3797` n `8`; equity avg `0.4901` n `162`; fx avg `0.0308` n `6`; index avg `0.048` n `27`; metal avg `0.0802` n `20`; unknown avg `3.0955` n `1252`
- 24h: commodity avg `0.1174` n `13`; crypto_alt avg `-0.4207` n `239`; crypto_major avg `0.1091` n `8`; equity avg `0.5848` n `162`; fx avg `0.0019` n `6`; index avg `0.0937` n `27`; metal avg `-0.0533` n `20`; unknown avg `2.953` n `1134`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
