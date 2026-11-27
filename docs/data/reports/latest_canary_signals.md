# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T11:52:24.022805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0339` n `13`; crypto_alt avg `-0.0201` n `239`; crypto_major avg `-0.1435` n `8`; equity avg `-0.3695` n `168`; fx avg `0.0066` n `6`; index avg `-0.0481` n `27`; metal avg `-0.0616` n `20`; unknown avg `1.3705` n `1261`
- 1h: commodity avg `-0.0012` n `13`; crypto_alt avg `-0.1643` n `239`; crypto_major avg `-0.2459` n `8`; equity avg `-0.8152` n `168`; fx avg `0.0018` n `6`; index avg `-0.0756` n `27`; metal avg `-0.1112` n `20`; unknown avg `0.8525` n `1253`
- 4h: commodity avg `-0.2716` n `13`; crypto_alt avg `-0.0179` n `239`; crypto_major avg `-0.0127` n `8`; equity avg `-0.0582` n `168`; fx avg `-0.0236` n `6`; index avg `-0.0174` n `27`; metal avg `-0.1133` n `20`; unknown avg `180.1868` n `1119`
- 24h: commodity avg `0.0433` n `13`; crypto_alt avg `1.591` n `239`; crypto_major avg `2.7413` n `8`; equity avg `3.2047` n `168`; fx avg `-0.0897` n `6`; index avg `0.2314` n `27`; metal avg `1.178` n `20`; unknown avg `261.7789` n `1025`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
