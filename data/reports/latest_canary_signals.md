# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T09:37:29.715547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0482` n `13`; crypto_alt avg `0.4815` n `239`; crypto_major avg `0.1676` n `8`; equity avg `0.1619` n `158`; fx avg `0.0005` n `6`; index avg `0.0161` n `27`; metal avg `0.0321` n `20`; unknown avg `0.9038` n `1263`
- 1h: commodity avg `0.152` n `13`; crypto_alt avg `1.0872` n `239`; crypto_major avg `0.3892` n `8`; equity avg `0.3009` n `158`; fx avg `-0.0092` n `6`; index avg `0.0202` n `27`; metal avg `0.0205` n `20`; unknown avg `154.9246` n `1247`
- 4h: commodity avg `-0.0959` n `13`; crypto_alt avg `0.5259` n `239`; crypto_major avg `-0.2128` n `8`; equity avg `-0.3873` n `158`; fx avg `0.0221` n `6`; index avg `-0.0711` n `27`; metal avg `-0.1847` n `20`; unknown avg `173.8056` n `1109`
- 24h: commodity avg `-0.1369` n `13`; crypto_alt avg `-1.4918` n `239`; crypto_major avg `-3.1108` n `8`; equity avg `-0.5436` n `158`; fx avg `-0.0973` n `6`; index avg `-0.0481` n `27`; metal avg `0.2684` n `20`; unknown avg `0.9225` n `1012`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
