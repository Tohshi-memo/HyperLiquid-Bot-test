# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T09:22:20.536493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0401` n `12`; crypto_alt avg `-0.3146` n `228`; crypto_major avg `-0.2898` n `8`; equity avg `-0.1869` n `66`; fx avg `-0.0024` n `6`; index avg `-0.1715` n `23`; metal avg `0.1966` n `18`; unknown avg `-0.1292` n `383`
- 1h: commodity avg `0.0688` n `12`; crypto_alt avg `-0.4242` n `228`; crypto_major avg `-0.2789` n `8`; equity avg `-0.39` n `66`; fx avg `-0.0639` n `6`; index avg `-0.2167` n `23`; metal avg `-0.1073` n `18`; unknown avg `-0.201` n `383`
- 4h: commodity avg `0.1904` n `12`; crypto_alt avg `-0.0481` n `228`; crypto_major avg `0.1966` n `8`; equity avg `0.0413` n `66`; fx avg `-0.0651` n `6`; index avg `-0.1123` n `23`; metal avg `-0.0631` n `18`; unknown avg `-0.167` n `363`
- 24h: commodity avg `0.6061` n `12`; crypto_alt avg `1.2048` n `228`; crypto_major avg `0.6689` n `8`; equity avg `-1.7459` n `66`; fx avg `0.2425` n `6`; index avg `-0.7844` n `23`; metal avg `-0.2569` n `18`; unknown avg `0.6533` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
