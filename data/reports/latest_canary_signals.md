# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T20:22:26.443600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0644` n `12`; crypto_alt avg `0.1321` n `228`; crypto_major avg `0.0884` n `8`; equity avg `0.0984` n `74`; fx avg `-0.0082` n `6`; index avg `0.0318` n `23`; metal avg `0.1115` n `18`; unknown avg `-0.0472` n `643`
- 1h: commodity avg `0.238` n `12`; crypto_alt avg `-0.0672` n `228`; crypto_major avg `-0.2496` n `8`; equity avg `-0.1281` n `74`; fx avg `-0.0222` n `6`; index avg `0.0175` n `23`; metal avg `0.1484` n `18`; unknown avg `-0.2318` n `643`
- 4h: commodity avg `-0.0671` n `12`; crypto_alt avg `-0.1214` n `228`; crypto_major avg `-0.1358` n `8`; equity avg `0.0428` n `74`; fx avg `-0.0111` n `6`; index avg `0.1525` n `23`; metal avg `0.1634` n `18`; unknown avg `-0.3949` n `643`
- 24h: commodity avg `-0.5261` n `12`; crypto_alt avg `-0.0711` n `228`; crypto_major avg `0.5774` n `8`; equity avg `-0.1743` n `74`; fx avg `0.0151` n `6`; index avg `0.4911` n `23`; metal avg `0.4794` n `18`; unknown avg `40.0675` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
