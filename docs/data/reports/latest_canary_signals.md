# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T11:37:23.209477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0557` n `12`; crypto_alt avg `-0.08` n `230`; crypto_major avg `-0.0944` n `8`; equity avg `-0.05` n `96`; fx avg `-0.0071` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0121` n `770`
- 1h: crypto_alt avg `0.0629` n `225`; crypto_major avg `0.149` n `7`; metal avg `0.0025` n `1`; unknown avg `-0.0275` n `703`
- 4h: commodity avg `0.017` n `12`; crypto_alt avg `-0.0463` n `230`; crypto_major avg `0.1002` n `8`; equity avg `-0.0132` n `96`; fx avg `-0.003` n `6`; index avg `0.0231` n `25`; metal avg `-0.0448` n `20`; unknown avg `-0.0165` n `770`
- 24h: commodity avg `0.1923` n `12`; crypto_alt avg `0.4505` n `230`; crypto_major avg `1.1994` n `8`; equity avg `0.1801` n `96`; fx avg `-0.0032` n `6`; index avg `-0.0491` n `25`; metal avg `-0.0908` n `20`; unknown avg `0.1285` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1129`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1121`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.095`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
