# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T20:52:38.735986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0685` n `13`; crypto_alt avg `0.1825` n `238`; crypto_major avg `-0.0163` n `8`; equity avg `0.01` n `156`; fx avg `0.0087` n `6`; index avg `-0.0055` n `27`; metal avg `-0.0007` n `20`; unknown avg `0.3234` n `1261`
- 1h: commodity avg `-0.1576` n `13`; crypto_alt avg `-0.0505` n `238`; crypto_major avg `-0.0963` n `8`; equity avg `0.0677` n `156`; fx avg `-0.0026` n `6`; index avg `-0.0079` n `27`; metal avg `-0.0654` n `20`; unknown avg `0.5267` n `1163`
- 4h: commodity avg `-0.3661` n `13`; crypto_alt avg `0.128` n `238`; crypto_major avg `-0.2136` n `8`; equity avg `0.5372` n `156`; fx avg `0.0126` n `6`; index avg `0.0277` n `27`; metal avg `-0.119` n `20`; unknown avg `1.4694` n `1165`
- 24h: commodity avg `0.0142` n `13`; crypto_alt avg `0.0453` n `238`; crypto_major avg `-1.199` n `8`; equity avg `-3.6254` n `156`; fx avg `-0.1012` n `6`; index avg `-0.3632` n `27`; metal avg `-1.0157` n `20`; unknown avg `1.5499` n `1022`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
