# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T22:07:32.311334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `13`; crypto_alt avg `0.0804` n `239`; crypto_major avg `0.0588` n `8`; equity avg `0.0046` n `168`; fx avg `-0.0048` n `6`; index avg `0.003` n `27`; metal avg `0.0094` n `20`; unknown avg `0.9912` n `1246`
- 1h: commodity avg `0.1154` n `13`; crypto_alt avg `-0.0901` n `239`; crypto_major avg `-0.0511` n `8`; equity avg `0.0005` n `168`; fx avg `-0.0036` n `6`; index avg `0.0041` n `27`; metal avg `0.0143` n `20`; unknown avg `40.3892` n `1248`
- 4h: commodity avg `0.2638` n `13`; crypto_alt avg `0.0011` n `239`; crypto_major avg `0.1129` n `8`; equity avg `0.2547` n `168`; fx avg `-0.0016` n `6`; index avg `0.026` n `27`; metal avg `0.0416` n `20`; unknown avg `102.9431` n `1182`
- 24h: commodity avg `0.0994` n `13`; crypto_alt avg `-3.2957` n `239`; crypto_major avg `-1.018` n `8`; equity avg `0.0106` n `168`; fx avg `-0.0108` n `6`; index avg `-0.0284` n `27`; metal avg `0.052` n `20`; unknown avg `2.3676` n `1087`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
