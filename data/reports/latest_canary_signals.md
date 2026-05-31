# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T21:52:16.155138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0355` n `12`; crypto_alt avg `0.4222` n `228`; crypto_major avg `0.2027` n `8`; equity avg `-0.0491` n `69`; fx avg `-0.0058` n `6`; index avg `0.1375` n `23`; metal avg `0.0167` n `18`; unknown avg `-0.0191` n `421`
- 1h: commodity avg `0.0135` n `12`; crypto_alt avg `0.7637` n `228`; crypto_major avg `0.5641` n `8`; equity avg `0.0416` n `69`; fx avg `-0.0104` n `6`; index avg `-0.0343` n `23`; metal avg `0.0415` n `18`; unknown avg `-0.04` n `421`
- 4h: commodity avg `-0.1468` n `12`; crypto_alt avg `1.2236` n `228`; crypto_major avg `0.619` n `8`; equity avg `0.0654` n `69`; fx avg `-0.0219` n `6`; index avg `0.1924` n `23`; metal avg `0.0276` n `18`; unknown avg `0.7064` n `421`
- 24h: commodity avg `0.402` n `12`; crypto_alt avg `-0.1419` n `228`; crypto_major avg `0.1205` n `8`; equity avg `0.7253` n `69`; fx avg `-0.0391` n `6`; index avg `0.3907` n `23`; metal avg `-0.1297` n `18`; unknown avg `1.101` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2966`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2048`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
