# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T03:07:23.144945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `13`; crypto_alt avg `0.3772` n `239`; crypto_major avg `0.3194` n `8`; equity avg `0.1448` n `158`; fx avg `0.0063` n `6`; index avg `0.0041` n `27`; metal avg `0.0119` n `20`; unknown avg `0.563` n `1258`
- 1h: commodity avg `0.0148` n `13`; crypto_alt avg `0.1158` n `239`; crypto_major avg `0.1471` n `8`; equity avg `0.1366` n `158`; fx avg `-0.0006` n `6`; index avg `0.0068` n `27`; metal avg `0.0084` n `20`; unknown avg `-0.0549` n `1254`
- 4h: commodity avg `-0.0356` n `13`; crypto_alt avg `-0.3235` n `239`; crypto_major avg `0.0777` n `8`; equity avg `0.0918` n `158`; fx avg `0.0345` n `6`; index avg `0.0086` n `27`; metal avg `-0.0073` n `20`; unknown avg `-0.1963` n `1246`
- 24h: commodity avg `0.0721` n `13`; crypto_alt avg `-1.7034` n `239`; crypto_major avg `-0.8556` n `8`; equity avg `-0.0073` n `158`; fx avg `0.0191` n `6`; index avg `0.05` n `27`; metal avg `-0.0492` n `20`; unknown avg `161.2755` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
