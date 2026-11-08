# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T01:07:25.734126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `13`; crypto_alt avg `0.0066` n `239`; crypto_major avg `0.018` n `8`; equity avg `-0.0383` n `158`; fx avg `-0.0045` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0031` n `20`; unknown avg `-0.0768` n `1258`
- 1h: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.2456` n `239`; crypto_major avg `-0.1298` n `8`; equity avg `-0.0825` n `158`; fx avg `-0.0021` n `6`; index avg `-0.0106` n `27`; metal avg `-0.0056` n `20`; unknown avg `-0.1513` n `1256`
- 4h: commodity avg `-0.0746` n `13`; crypto_alt avg `0.424` n `239`; crypto_major avg `0.4245` n `8`; equity avg `0.0779` n `158`; fx avg `0.0035` n `6`; index avg `-0.0028` n `27`; metal avg `0.0004` n `20`; unknown avg `0.4485` n `1228`
- 24h: commodity avg `0.0064` n `13`; crypto_alt avg `-1.7414` n `239`; crypto_major avg `-0.8067` n `8`; equity avg `-0.3322` n `158`; fx avg `-0.0074` n `6`; index avg `0.0253` n `27`; metal avg `-0.0408` n `20`; unknown avg `160.5334` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
