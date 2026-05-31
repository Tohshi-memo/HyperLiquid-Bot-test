# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T11:07:22.802078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.2215` n `228`; crypto_major avg `0.0925` n `8`; equity avg `0.042` n `69`; fx avg `-0.0249` n `6`; index avg `0.0137` n `23`; metal avg `-0.0041` n `18`; unknown avg `0.0902` n `421`
- 1h: commodity avg `0.1234` n `12`; crypto_alt avg `0.2601` n `228`; crypto_major avg `-0.0291` n `8`; equity avg `-0.0285` n `69`; fx avg `-0.0223` n `6`; index avg `0.0394` n `23`; metal avg `0.0054` n `18`; unknown avg `-0.3011` n `421`
- 4h: commodity avg `0.0333` n `12`; crypto_alt avg `-0.1192` n `228`; crypto_major avg `-0.471` n `8`; equity avg `0.1247` n `69`; fx avg `-0.0445` n `6`; index avg `-0.0756` n `23`; metal avg `-0.0352` n `18`; unknown avg `-0.3298` n `421`
- 24h: commodity avg `0.2624` n `12`; crypto_alt avg `0.2425` n `228`; crypto_major avg `1.2463` n `8`; equity avg `1.055` n `69`; fx avg `-0.0055` n `6`; index avg `-0.061` n `23`; metal avg `-0.0952` n `18`; unknown avg `0.6371` n `401`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
