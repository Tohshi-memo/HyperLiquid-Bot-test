# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T11:22:27.450615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `13`; crypto_alt avg `0.3163` n `237`; crypto_major avg `0.2408` n `8`; equity avg `0.0935` n `152`; fx avg `0.0` n `6`; index avg `0.0041` n `26`; metal avg `0.0057` n `20`; unknown avg `-0.0101` n `1231`
- 1h: commodity avg `0.0435` n `13`; crypto_alt avg `0.1115` n `237`; crypto_major avg `0.2002` n `8`; equity avg `0.0968` n `152`; fx avg `0.02` n `6`; index avg `-0.0029` n `26`; metal avg `0.0113` n `20`; unknown avg `1.694` n `1227`
- 4h: commodity avg `-0.0638` n `13`; crypto_alt avg `-0.4922` n `237`; crypto_major avg `-0.3152` n `8`; equity avg `-0.0344` n `152`; fx avg `0.0182` n `6`; index avg `-0.011` n `26`; metal avg `0.0009` n `20`; unknown avg `20.6992` n `1181`
- 24h: commodity avg `0.0171` n `13`; crypto_alt avg `-1.5926` n `237`; crypto_major avg `0.0006` n `8`; equity avg `0.0622` n `152`; fx avg `-0.0062` n `6`; index avg `0.0223` n `26`; metal avg `-0.0357` n `20`; unknown avg `22.8515` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1983`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
