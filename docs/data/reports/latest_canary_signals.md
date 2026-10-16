# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T11:22:38.175549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `13`; crypto_alt avg `0.2967` n `236`; crypto_major avg `0.395` n `8`; equity avg `0.0923` n `151`; fx avg `0.0022` n `6`; index avg `0.0155` n `26`; metal avg `0.0456` n `20`; unknown avg `1.2684` n `1136`
- 1h: commodity avg `0.0919` n `13`; crypto_alt avg `0.3853` n `236`; crypto_major avg `0.7993` n `8`; equity avg `-0.1001` n `151`; fx avg `0.0338` n `6`; index avg `0.0024` n `26`; metal avg `0.021` n `20`; unknown avg `2.9907` n `1134`
- 4h: commodity avg `0.0487` n `13`; crypto_alt avg `-0.0417` n `236`; crypto_major avg `0.543` n `8`; equity avg `-0.4834` n `151`; fx avg `0.0457` n `6`; index avg `-0.0327` n `26`; metal avg `-0.0229` n `20`; unknown avg `0.4218` n `1066`
- 24h: commodity avg `0.0565` n `13`; crypto_alt avg `4.7955` n `236`; crypto_major avg `3.0009` n `8`; equity avg `2.5596` n `151`; fx avg `0.0248` n `6`; index avg `0.3416` n `26`; metal avg `0.3097` n `20`; unknown avg `25.3018` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0965`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0921`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.091`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0829`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
