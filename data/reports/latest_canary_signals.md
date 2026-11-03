# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T17:53:29.953109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `-0.0042` n `239`; crypto_major avg `0.1331` n `8`; equity avg `0.0484` n `158`; fx avg `0.0008` n `6`; index avg `0.0261` n `27`; metal avg `0.0237` n `20`; unknown avg `0.0116` n `1263`
- 1h: commodity avg `0.0335` n `13`; crypto_alt avg `-0.1385` n `239`; crypto_major avg `0.0199` n `8`; equity avg `0.2156` n `158`; fx avg `0.0077` n `6`; index avg `0.0249` n `27`; metal avg `0.0026` n `20`; unknown avg `0.0115` n `1257`
- 4h: commodity avg `0.3922` n `13`; crypto_alt avg `-0.1358` n `239`; crypto_major avg `0.2864` n `8`; equity avg `0.322` n `158`; fx avg `0.0864` n `6`; index avg `-0.0248` n `27`; metal avg `-0.3544` n `20`; unknown avg `447.0913` n `1253`
- 24h: commodity avg `0.1899` n `13`; crypto_alt avg `0.9717` n `239`; crypto_major avg `1.6678` n `8`; equity avg `0.2859` n `158`; fx avg `0.0587` n `6`; index avg `0.012` n `27`; metal avg `-0.5421` n `20`; unknown avg `0.2699` n `1021`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
