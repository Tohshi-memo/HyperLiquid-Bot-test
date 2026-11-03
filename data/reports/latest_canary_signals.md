# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T21:52:58.649921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `13`; crypto_alt avg `-0.0139` n `239`; crypto_major avg `-0.0788` n `8`; equity avg `-0.1012` n `158`; fx avg `-0.0035` n `6`; index avg `-0.0119` n `27`; metal avg `-0.0109` n `20`; unknown avg `158.8941` n `1262`
- 1h: commodity avg `0.0518` n `13`; crypto_alt avg `0.3897` n `239`; crypto_major avg `0.1781` n `8`; equity avg `1.0053` n `158`; fx avg `0.0055` n `6`; index avg `0.1106` n `27`; metal avg `0.0533` n `20`; unknown avg `0.3772` n `1249`
- 4h: commodity avg `0.2264` n `13`; crypto_alt avg `0.4272` n `239`; crypto_major avg `0.0817` n `8`; equity avg `0.8816` n `158`; fx avg `0.0181` n `6`; index avg `0.0622` n `27`; metal avg `-0.0341` n `20`; unknown avg `-0.8607` n `1175`
- 24h: commodity avg `0.4223` n `13`; crypto_alt avg `1.04` n `239`; crypto_major avg `1.3605` n `8`; equity avg `2.4707` n `158`; fx avg `0.0827` n `6`; index avg `0.2485` n `27`; metal avg `-0.5042` n `20`; unknown avg `-0.6812` n `1063`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
