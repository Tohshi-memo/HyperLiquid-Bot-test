# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T22:52:17.139989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `-0.0688` n `228`; crypto_major avg `-0.0028` n `8`; equity avg `-0.0129` n `66`; fx avg `-0.0017` n `6`; index avg `-0.0274` n `23`; metal avg `-0.054` n `18`; unknown avg `-0.2314` n `383`
- 1h: commodity avg `0.0743` n `12`; crypto_alt avg `-0.6195` n `228`; crypto_major avg `-0.3051` n `8`; equity avg `-0.1536` n `66`; fx avg `-0.0074` n `6`; index avg `-0.0865` n `23`; metal avg `-0.0112` n `18`; unknown avg `-0.0938` n `383`
- 4h: commodity avg `-0.1844` n `12`; crypto_alt avg `-0.6372` n `228`; crypto_major avg `-0.416` n `8`; equity avg `-0.4684` n `66`; fx avg `-0.0077` n `6`; index avg `-0.2227` n `23`; metal avg `-0.2921` n `18`; unknown avg `-0.3747` n `383`
- 24h: commodity avg `1.0825` n `12`; crypto_alt avg `-1.1015` n `228`; crypto_major avg `-0.7189` n `8`; equity avg `-0.3229` n `66`; fx avg `0.0596` n `6`; index avg `-0.7916` n `23`; metal avg `-2.945` n `18`; unknown avg `0.9003` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
