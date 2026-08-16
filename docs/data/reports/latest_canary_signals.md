# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T15:37:27.577708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `0.0462` n `230`; crypto_major avg `0.0364` n `8`; equity avg `0.0279` n `114`; fx avg `-0.003` n `6`; index avg `0.0011` n `25`; metal avg `-0.004` n `20`; unknown avg `0.0455` n `791`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `0.1248` n `230`; crypto_major avg `0.0798` n `8`; equity avg `0.0408` n `114`; fx avg `0.0081` n `6`; index avg `-0.0072` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.0539` n `791`
- 4h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.1402` n `230`; crypto_major avg `0.1835` n `8`; equity avg `0.0397` n `114`; fx avg `0.0014` n `6`; index avg `-0.0046` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.0861` n `791`
- 24h: commodity avg `0.0638` n `12`; crypto_alt avg `-0.1641` n `230`; crypto_major avg `0.0537` n `8`; equity avg `0.296` n `114`; fx avg `-0.0058` n `6`; index avg `0.0232` n `25`; metal avg `0.0291` n `20`; unknown avg `0.1639` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.215`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
