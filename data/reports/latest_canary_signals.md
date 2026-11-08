# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T09:07:25.628634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `13`; crypto_alt avg `-0.1089` n `239`; crypto_major avg `0.0096` n `8`; equity avg `-0.0173` n `158`; fx avg `0.0091` n `6`; index avg `-0.0082` n `27`; metal avg `0.0073` n `20`; unknown avg `-0.0378` n `1258`
- 1h: commodity avg `-0.0079` n `13`; crypto_alt avg `-0.0798` n `239`; crypto_major avg `-0.0317` n `8`; equity avg `-0.0125` n `158`; fx avg `-0.0034` n `6`; index avg `-0.022` n `27`; metal avg `0.0042` n `20`; unknown avg `-0.0414` n `1256`
- 4h: commodity avg `0.0306` n `13`; crypto_alt avg `-0.044` n `239`; crypto_major avg `0.0433` n `8`; equity avg `0.1333` n `158`; fx avg `0.0154` n `6`; index avg `0.0066` n `27`; metal avg `0.0207` n `20`; unknown avg `0.0533` n `1204`
- 24h: commodity avg `0.1183` n `13`; crypto_alt avg `-1.6847` n `239`; crypto_major avg `-0.7458` n `8`; equity avg `-0.2377` n `158`; fx avg `0.0556` n `6`; index avg `-0.0069` n `27`; metal avg `-0.0285` n `20`; unknown avg `145.6153` n `1119`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
