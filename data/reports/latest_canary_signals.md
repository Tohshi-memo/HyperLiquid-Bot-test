# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T11:37:32.355039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `0.1056` n `239`; crypto_major avg `0.0725` n `8`; equity avg `-0.0037` n `158`; fx avg `0.0001` n `6`; index avg `0.0038` n `27`; metal avg `-0.0036` n `20`; unknown avg `-0.0667` n `1261`
- 1h: commodity avg `0.0288` n `13`; crypto_alt avg `0.0799` n `239`; crypto_major avg `0.1354` n `8`; equity avg `0.0298` n `158`; fx avg `-0.0062` n `6`; index avg `0.0086` n `27`; metal avg `-0.0067` n `20`; unknown avg `-0.0363` n `1255`
- 4h: commodity avg `0.0647` n `13`; crypto_alt avg `-0.7179` n `239`; crypto_major avg `-0.1357` n `8`; equity avg `0.1035` n `158`; fx avg `0.0006` n `6`; index avg `0.0109` n `27`; metal avg `-0.0023` n `20`; unknown avg `136.0884` n `1199`
- 24h: commodity avg `-0.1003` n `13`; crypto_alt avg `-1.492` n `239`; crypto_major avg `-0.5349` n `8`; equity avg `-0.603` n `158`; fx avg `-0.0279` n `6`; index avg `-0.0201` n `27`; metal avg `-0.0041` n `20`; unknown avg `7.5963` n `1059`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
