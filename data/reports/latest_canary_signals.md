# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T18:52:29.962611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0984` n `13`; crypto_alt avg `0.187` n `239`; crypto_major avg `0.141` n `8`; equity avg `0.1056` n `168`; fx avg `-0.0091` n `6`; index avg `0.0073` n `27`; metal avg `0.0065` n `20`; unknown avg `1.5978` n `1268`
- 1h: commodity avg `0.0919` n `13`; crypto_alt avg `0.3348` n `239`; crypto_major avg `0.3119` n `8`; equity avg `0.1805` n `168`; fx avg `-0.0068` n `6`; index avg `0.0106` n `27`; metal avg `0.0176` n `20`; unknown avg `0.3979` n `1242`
- 4h: commodity avg `0.0494` n `13`; crypto_alt avg `-0.6302` n `239`; crypto_major avg `-0.0425` n `8`; equity avg `0.0893` n `168`; fx avg `-0.0136` n `6`; index avg `0.0024` n `27`; metal avg `-0.0173` n `20`; unknown avg `41.079` n `1205`
- 24h: commodity avg `0.0433` n `13`; crypto_alt avg `-2.9047` n `239`; crypto_major avg `-1.0858` n `8`; equity avg `0.0223` n `168`; fx avg `-0.0111` n `6`; index avg `-0.013` n `27`; metal avg `0.2026` n `20`; unknown avg `186.8315` n `1071`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
