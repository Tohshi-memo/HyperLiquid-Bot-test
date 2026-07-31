# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T23:47:46.350196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0402` n `12`; crypto_alt avg `-0.0895` n `230`; crypto_major avg `-0.0551` n `8`; equity avg `-0.0124` n `102`; fx avg `-0.0223` n `6`; index avg `-0.0126` n `25`; metal avg `-0.0002` n `20`; unknown avg `5.4304` n `781`
- 1h: commodity avg `0.0156` n `12`; crypto_alt avg `0.0843` n `230`; crypto_major avg `-0.0239` n `8`; equity avg `-0.0157` n `102`; fx avg `-0.0403` n `6`; index avg `-0.0345` n `25`; metal avg `-0.0067` n `20`; unknown avg `3.9135` n `781`
- 4h: commodity avg `0.5602` n `12`; crypto_alt avg `-0.0447` n `230`; crypto_major avg `-0.1305` n `8`; equity avg `-0.6983` n `102`; fx avg `-0.1405` n `6`; index avg `-0.1567` n `25`; metal avg `-0.0795` n `20`; unknown avg `5.5395` n `780`
- 24h: commodity avg `0.7801` n `12`; crypto_alt avg `-0.5427` n `230`; crypto_major avg `-2.3043` n `8`; equity avg `-1.9709` n `102`; fx avg `0.0439` n `6`; index avg `-0.052` n `25`; metal avg `-0.4314` n `20`; unknown avg `2.6497` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
