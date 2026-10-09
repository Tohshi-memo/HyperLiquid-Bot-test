# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T20:52:36.208546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `13`; crypto_alt avg `0.2647` n `235`; crypto_major avg `0.1624` n `8`; equity avg `0.0243` n `150`; fx avg `0.0047` n `6`; index avg `0.0151` n `26`; metal avg `0.0053` n `20`; unknown avg `4.6726` n `1116`
- 1h: commodity avg `0.0511` n `13`; crypto_alt avg `0.7466` n `235`; crypto_major avg `0.342` n `8`; equity avg `0.1328` n `150`; fx avg `0.0124` n `6`; index avg `0.0255` n `26`; metal avg `0.0373` n `20`; unknown avg `4.3645` n `1040`
- 4h: commodity avg `-0.1902` n `13`; crypto_alt avg `-0.3033` n `235`; crypto_major avg `-0.3947` n `8`; equity avg `0.0869` n `150`; fx avg `0.0274` n `6`; index avg `0.0165` n `26`; metal avg `0.032` n `20`; unknown avg `4.163` n `1040`
- 24h: commodity avg `-0.1167` n `13`; crypto_alt avg `1.3253` n `235`; crypto_major avg `0.213` n `8`; equity avg `0.8978` n `150`; fx avg `0.0254` n `6`; index avg `0.1566` n `26`; metal avg `0.6293` n `20`; unknown avg `13.3943` n `909`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
