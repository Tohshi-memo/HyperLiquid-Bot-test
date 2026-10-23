# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T17:52:33.537991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0348` n `13`; crypto_alt avg `0.0394` n `237`; crypto_major avg `-0.0288` n `8`; equity avg `0.0633` n `152`; fx avg `0.0146` n `6`; index avg `0.0199` n `26`; metal avg `0.0161` n `20`; unknown avg `-0.1508` n `1229`
- 1h: commodity avg `0.0715` n `13`; crypto_alt avg `-0.254` n `237`; crypto_major avg `-0.2111` n `8`; equity avg `-0.0943` n `152`; fx avg `-0.012` n `6`; index avg `-0.0149` n `26`; metal avg `-0.0776` n `20`; unknown avg `-0.6408` n `1229`
- 4h: commodity avg `0.0457` n `13`; crypto_alt avg `-0.1459` n `237`; crypto_major avg `-0.3486` n `8`; equity avg `0.2412` n `152`; fx avg `0.0103` n `6`; index avg `0.0648` n `26`; metal avg `-0.0865` n `20`; unknown avg `-0.7127` n `1157`
- 24h: commodity avg `0.1847` n `13`; crypto_alt avg `1.0484` n `237`; crypto_major avg `0.903` n `8`; equity avg `1.3578` n `152`; fx avg `-0.1101` n `6`; index avg `0.0517` n `26`; metal avg `-0.2386` n `20`; unknown avg `-0.9012` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
