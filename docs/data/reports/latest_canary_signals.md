# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T20:22:29.537428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0413` n `12`; crypto_alt avg `0.0003` n `230`; crypto_major avg `0.0706` n `8`; equity avg `0.0297` n `102`; fx avg `0.0011` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0102` n `20`; unknown avg `-0.0707` n `782`
- 1h: commodity avg `0.0315` n `12`; crypto_alt avg `0.2299` n `230`; crypto_major avg `0.1704` n `8`; equity avg `-0.0228` n `102`; fx avg `0.0104` n `6`; index avg `-0.0281` n `25`; metal avg `-0.0225` n `20`; unknown avg `-0.0557` n `782`
- 4h: commodity avg `0.0444` n `12`; crypto_alt avg `-1.0573` n `230`; crypto_major avg `-1.0279` n `8`; equity avg `-0.2528` n `102`; fx avg `0.0005` n `6`; index avg `-0.0418` n `25`; metal avg `0.0003` n `20`; unknown avg `2.8296` n `782`
- 24h: commodity avg `0.6232` n `12`; crypto_alt avg `-0.7932` n `230`; crypto_major avg `-1.2681` n `8`; equity avg `-0.7137` n `102`; fx avg `-0.0889` n `6`; index avg `-0.1047` n `25`; metal avg `-0.0358` n `20`; unknown avg `4.3` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
