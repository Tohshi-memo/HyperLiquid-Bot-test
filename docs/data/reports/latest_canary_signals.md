# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T00:07:29.565641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0984` n `13`; crypto_alt avg `-0.0707` n `238`; crypto_major avg `-0.0055` n `8`; equity avg `0.0556` n `156`; fx avg `0.0291` n `6`; index avg `0.0361` n `27`; metal avg `0.0094` n `20`; unknown avg `0.1098` n `1249`
- 1h: commodity avg `0.1139` n `13`; crypto_alt avg `0.2541` n `238`; crypto_major avg `0.5089` n `8`; equity avg `0.4787` n `156`; fx avg `0.0088` n `6`; index avg `0.1079` n `27`; metal avg `0.1313` n `20`; unknown avg `0.8585` n `1249`
- 4h: commodity avg `0.0539` n `13`; crypto_alt avg `0.3794` n `238`; crypto_major avg `0.5609` n `8`; equity avg `0.3666` n `156`; fx avg `0.0221` n `6`; index avg `0.0803` n `27`; metal avg `0.1655` n `20`; unknown avg `7.8021` n `1219`
- 24h: commodity avg `0.0031` n `13`; crypto_alt avg `-0.4223` n `238`; crypto_major avg `0.2654` n `8`; equity avg `0.6034` n `156`; fx avg `0.0317` n `6`; index avg `0.1196` n `27`; metal avg `0.1821` n `20`; unknown avg `3.6339` n `1082`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
