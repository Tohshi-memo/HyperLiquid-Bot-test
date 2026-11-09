# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T16:07:31.167006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.9467` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0108` n `13`; crypto_alt avg `-0.2489` n `239`; crypto_major avg `-0.3078` n `8`; equity avg `0.1618` n `160`; fx avg `0.0004` n `6`; index avg `0.0035` n `27`; metal avg `0.0732` n `20`; unknown avg `-0.0307` n `1251`
- 1h: commodity avg `0.1665` n `13`; crypto_alt avg `0.5849` n `239`; crypto_major avg `0.5034` n `8`; equity avg `1.5377` n `160`; fx avg `-0.0205` n `6`; index avg `0.0953` n `27`; metal avg `0.1526` n `20`; unknown avg `-0.022` n `1249`
- 4h: commodity avg `0.2896` n `13`; crypto_alt avg `1.6734` n `239`; crypto_major avg `1.3762` n `8`; equity avg `4.3229` n `160`; fx avg `0.0141` n `6`; index avg `0.4287` n `27`; metal avg `0.2104` n `20`; unknown avg `23.733` n `1249`
- 24h: commodity avg `-0.2481` n `13`; crypto_alt avg `0.846` n `239`; crypto_major avg `-2.135` n `8`; equity avg `4.2001` n `160`; fx avg `-0.1575` n `6`; index avg `0.4397` n `27`; metal avg `0.5475` n `20`; unknown avg `6.3533` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
