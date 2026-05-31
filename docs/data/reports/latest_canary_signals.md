# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T19:52:17.767573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.076` n `12`; crypto_alt avg `0.2479` n `228`; crypto_major avg `0.1312` n `8`; equity avg `0.0342` n `69`; fx avg `0.0007` n `6`; index avg `-0.0954` n `23`; metal avg `0.0017` n `18`; unknown avg `0.06` n `421`
- 1h: commodity avg `0.0332` n `12`; crypto_alt avg `0.0605` n `228`; crypto_major avg `-0.0348` n `8`; equity avg `0.015` n `69`; fx avg `-0.002` n `6`; index avg `0.1131` n `23`; metal avg `-0.0068` n `18`; unknown avg `-0.2614` n `421`
- 4h: commodity avg `0.1219` n `12`; crypto_alt avg `-0.005` n `228`; crypto_major avg `-0.3481` n `8`; equity avg `0.0726` n `69`; fx avg `0.0003` n `6`; index avg `0.3072` n `23`; metal avg `-0.0087` n `18`; unknown avg `0.132` n `421`
- 24h: commodity avg `0.7236` n `12`; crypto_alt avg `-1.2091` n `228`; crypto_major avg `-0.8346` n `8`; equity avg `0.8595` n `69`; fx avg `-0.0253` n `6`; index avg `0.2002` n `23`; metal avg `-0.1255` n `18`; unknown avg `0.1537` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2535`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
