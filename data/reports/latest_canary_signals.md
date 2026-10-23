# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T15:22:49.672238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `13`; crypto_alt avg `-0.2055` n `237`; crypto_major avg `-0.0952` n `8`; equity avg `-0.1718` n `152`; fx avg `-0.0182` n `6`; index avg `-0.0204` n `26`; metal avg `0.0485` n `20`; unknown avg `0.0645` n `1233`
- 1h: commodity avg `-0.1402` n `13`; crypto_alt avg `0.3604` n `237`; crypto_major avg `0.3342` n `8`; equity avg `0.3106` n `152`; fx avg `-0.0183` n `6`; index avg `0.113` n `26`; metal avg `0.178` n `20`; unknown avg `0.7311` n `1229`
- 4h: commodity avg `0.0005` n `13`; crypto_alt avg `-0.0938` n `237`; crypto_major avg `0.1517` n `8`; equity avg `0.15` n `152`; fx avg `0.0009` n `6`; index avg `0.0736` n `26`; metal avg `-0.044` n `20`; unknown avg `-0.2587` n `1161`
- 24h: commodity avg `0.425` n `13`; crypto_alt avg `0.725` n `237`; crypto_major avg `0.4421` n `8`; equity avg `-0.1566` n `152`; fx avg `-0.0715` n `6`; index avg `-0.0252` n `26`; metal avg `-0.248` n `20`; unknown avg `-0.7634` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
