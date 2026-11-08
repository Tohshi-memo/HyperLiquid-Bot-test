# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T21:37:26.354447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1045` n `13`; crypto_alt avg `-0.1144` n `239`; crypto_major avg `-0.1384` n `8`; equity avg `-0.0484` n `158`; fx avg `-0.0006` n `6`; index avg `-0.003` n `27`; metal avg `-0.0068` n `20`; unknown avg `0.2968` n `1262`
- 1h: commodity avg `0.0917` n `13`; crypto_alt avg `-0.3138` n `239`; crypto_major avg `-0.3494` n `8`; equity avg `-0.1961` n `158`; fx avg `-0.0164` n `6`; index avg `-0.0396` n `27`; metal avg `0.0038` n `20`; unknown avg `0.2925` n `1238`
- 4h: commodity avg `-0.0197` n `13`; crypto_alt avg `0.143` n `239`; crypto_major avg `-0.175` n `8`; equity avg `-0.1901` n `158`; fx avg `-0.0321` n `6`; index avg `-0.0593` n `27`; metal avg `0.0183` n `20`; unknown avg `13.0709` n `1164`
- 24h: commodity avg `0.0267` n `13`; crypto_alt avg `-1.1343` n `239`; crypto_major avg `-0.2414` n `8`; equity avg `0.0357` n `158`; fx avg `0.0421` n `6`; index avg `-0.0649` n `27`; metal avg `-0.0212` n `20`; unknown avg `-0.3154` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
