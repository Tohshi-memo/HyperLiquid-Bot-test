# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T21:22:31.756038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.162` n `13`; crypto_alt avg `0.1952` n `235`; crypto_major avg `0.0701` n `8`; equity avg `-0.0303` n `150`; fx avg `0.0039` n `6`; index avg `0.0` n `26`; metal avg `-0.0061` n `20`; unknown avg `0.3305` n `1116`
- 1h: commodity avg `-0.0513` n `13`; crypto_alt avg `0.3617` n `235`; crypto_major avg `0.2656` n `8`; equity avg `0.0045` n `150`; fx avg `-0.0019` n `6`; index avg `0.0102` n `26`; metal avg `-0.0142` n `20`; unknown avg `3.6258` n `1106`
- 4h: commodity avg `-0.2344` n `13`; crypto_alt avg `0.4407` n `235`; crypto_major avg `0.1353` n `8`; equity avg `0.147` n `150`; fx avg `0.007` n `6`; index avg `0.0376` n `26`; metal avg `0.0204` n `20`; unknown avg `3.3673` n `1034`
- 24h: commodity avg `-0.2394` n `13`; crypto_alt avg `1.765` n `235`; crypto_major avg `0.3536` n `8`; equity avg `0.882` n `150`; fx avg `0.0186` n `6`; index avg `0.1509` n `26`; metal avg `0.6044` n `20`; unknown avg `13.4755` n `909`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
