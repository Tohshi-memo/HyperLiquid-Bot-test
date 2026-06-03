# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T05:22:20.169503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0494` n `12`; crypto_alt avg `0.1513` n `228`; crypto_major avg `0.143` n `8`; equity avg `0.0555` n `72`; fx avg `0.0203` n `6`; index avg `0.0536` n `23`; metal avg `0.1285` n `18`; unknown avg `0.3319` n `420`
- 1h: commodity avg `-0.0816` n `12`; crypto_alt avg `1.871` n `228`; crypto_major avg `1.3241` n `8`; equity avg `0.1217` n `72`; fx avg `0.0038` n `6`; index avg `0.0376` n `23`; metal avg `-0.1597` n `18`; unknown avg `0.7965` n `420`
- 4h: commodity avg `-0.1588` n `12`; crypto_alt avg `1.4216` n `228`; crypto_major avg `0.6972` n `8`; equity avg `0.2855` n `72`; fx avg `0.0191` n `6`; index avg `0.0239` n `23`; metal avg `0.1918` n `18`; unknown avg `-0.0876` n `419`
- 24h: commodity avg `0.9593` n `12`; crypto_alt avg `-2.5121` n `228`; crypto_major avg `-4.4353` n `8`; equity avg `1.0223` n `72`; fx avg `0.0567` n `6`; index avg `1.3283` n `23`; metal avg `-0.6156` n `18`; unknown avg `-0.7189` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
