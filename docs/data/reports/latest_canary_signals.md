# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T20:22:26.332957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `13`; crypto_alt avg `0.0196` n `237`; crypto_major avg `0.0144` n `8`; equity avg `0.0416` n `152`; fx avg `0.002` n `6`; index avg `0.0077` n `26`; metal avg `0.0146` n `20`; unknown avg `1.1681` n `1230`
- 1h: commodity avg `0.051` n `13`; crypto_alt avg `-0.04` n `237`; crypto_major avg `-0.0529` n `8`; equity avg `-0.0077` n `152`; fx avg `0.0126` n `6`; index avg `-0.008` n `26`; metal avg `0.0045` n `20`; unknown avg `2.689` n `1172`
- 4h: commodity avg `0.0188` n `13`; crypto_alt avg `0.4552` n `237`; crypto_major avg `0.2178` n `8`; equity avg `0.2455` n `152`; fx avg `0.0292` n `6`; index avg `0.0369` n `26`; metal avg `0.0477` n `20`; unknown avg `0.9402` n `1164`
- 24h: commodity avg `-0.2165` n `13`; crypto_alt avg `-0.1188` n `237`; crypto_major avg `0.4567` n `8`; equity avg `0.5955` n `152`; fx avg `0.047` n `6`; index avg `0.1234` n `26`; metal avg `0.1374` n `20`; unknown avg `10.0822` n `1027`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2271`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
