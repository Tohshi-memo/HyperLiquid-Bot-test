# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T10:37:27.337027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0949` n `13`; crypto_alt avg `0.0744` n `237`; crypto_major avg `0.0656` n `8`; equity avg `0.0496` n `151`; fx avg `0.0021` n `6`; index avg `0.0133` n `26`; metal avg `0.0062` n `20`; unknown avg `3.8337` n `1193`
- 1h: commodity avg `-0.0263` n `13`; crypto_alt avg `-0.1474` n `237`; crypto_major avg `0.0434` n `8`; equity avg `-0.0245` n `151`; fx avg `-0.0019` n `6`; index avg `0.0094` n `26`; metal avg `0.0089` n `20`; unknown avg `4.1532` n `1191`
- 4h: commodity avg `-0.0143` n `13`; crypto_alt avg `-0.0453` n `237`; crypto_major avg `0.3213` n `8`; equity avg `0.2586` n `151`; fx avg `0.0002` n `6`; index avg `0.0641` n `26`; metal avg `0.0223` n `20`; unknown avg `5.0038` n `1079`
- 24h: commodity avg `0.0037` n `13`; crypto_alt avg `-2.2039` n `236`; crypto_major avg `-0.3359` n `8`; equity avg `-0.5992` n `151`; fx avg `-0.0527` n `6`; index avg `-0.0541` n `26`; metal avg `-0.0379` n `20`; unknown avg `4.61` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2009`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1356`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1298`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1139`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0796`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
