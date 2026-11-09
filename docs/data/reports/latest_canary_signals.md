# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T17:22:31.894672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-3.5197` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0165` n `13`; crypto_alt avg `-0.2681` n `239`; crypto_major avg `-0.1931` n `8`; equity avg `0.0003` n `160`; fx avg `0.0068` n `6`; index avg `0.0118` n `27`; metal avg `-0.0175` n `20`; unknown avg `7.6689` n `1261`
- 1h: commodity avg `0.0076` n `13`; crypto_alt avg `-0.4432` n `239`; crypto_major avg `-0.445` n `8`; equity avg `0.2427` n `160`; fx avg `0.0016` n `6`; index avg `0.0408` n `27`; metal avg `-0.0606` n `20`; unknown avg `0.191` n `1255`
- 4h: commodity avg `0.1092` n `13`; crypto_alt avg `0.1308` n `239`; crypto_major avg `0.3565` n `8`; equity avg `3.8762` n `160`; fx avg `-0.0033` n `6`; index avg `0.4107` n `27`; metal avg `-0.0038` n `20`; unknown avg `4.7918` n `1249`
- 24h: commodity avg `-0.3157` n `13`; crypto_alt avg `0.7644` n `239`; crypto_major avg `-2.4007` n `8`; equity avg `4.0519` n `160`; fx avg `-0.1516` n `6`; index avg `0.4408` n `27`; metal avg `0.4048` n `20`; unknown avg `6.5182` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
