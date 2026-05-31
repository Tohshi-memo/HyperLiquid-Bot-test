# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T20:52:19.242026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0435` n `12`; crypto_alt avg `0.0323` n `228`; crypto_major avg `0.0631` n `8`; equity avg `0.0079` n `69`; fx avg `0.0013` n `6`; index avg `0.2665` n `23`; metal avg `0.0034` n `18`; unknown avg `1.0082` n `421`
- 1h: commodity avg `-0.2174` n `12`; crypto_alt avg `0.4899` n `228`; crypto_major avg `0.352` n `8`; equity avg `-0.0317` n `69`; fx avg `-0.0079` n `6`; index avg `0.1727` n `23`; metal avg `-0.0173` n `18`; unknown avg `1.4402` n `421`
- 4h: commodity avg `-0.0226` n `12`; crypto_alt avg `1.1339` n `228`; crypto_major avg `0.6135` n `8`; equity avg `0.1364` n `69`; fx avg `-0.01` n `6`; index avg `0.4335` n `23`; metal avg `-0.0506` n `18`; unknown avg `1.3763` n `421`
- 24h: commodity avg `0.5522` n `12`; crypto_alt avg `-0.8688` n `228`; crypto_major avg `-0.3543` n `8`; equity avg `0.7426` n `69`; fx avg `-0.0303` n `6`; index avg `0.4289` n `23`; metal avg `-0.1566` n `18`; unknown avg `1.6301` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.276`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1951`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
