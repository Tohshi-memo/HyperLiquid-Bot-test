# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T14:36:22.202697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1268` n `13`; crypto_alt avg `0.534` n `237`; crypto_major avg `0.4388` n `8`; equity avg `0.5381` n `153`; fx avg `0.0192` n `6`; index avg `0.1259` n `26`; metal avg `0.1508` n `20`; unknown avg `362.5087` n `1192`
- 1h: commodity avg `-0.1953` n `13`; crypto_alt avg `0.069` n `237`; crypto_major avg `0.1325` n `8`; equity avg `0.1647` n `152`; fx avg `0.0145` n `6`; index avg `0.0484` n `26`; metal avg `0.0666` n `20`; unknown avg `331.818` n `1190`
- 4h: commodity avg `-0.1328` n `13`; crypto_alt avg `0.2581` n `237`; crypto_major avg `-0.0338` n `8`; equity avg `0.2184` n `152`; fx avg `0.0026` n `6`; index avg `0.1422` n `26`; metal avg `-0.0106` n `20`; unknown avg `343.932` n `1172`
- 24h: commodity avg `-0.5226` n `13`; crypto_alt avg `0.7253` n `237`; crypto_major avg `0.3108` n `8`; equity avg `-0.1933` n `152`; fx avg `0.0376` n `6`; index avg `0.1234` n `26`; metal avg `0.0928` n `20`; unknown avg `75.2438` n `933`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2311`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1968`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1916`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1803`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1365`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1292`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `669`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1088`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0958`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0765`, n `669`, weak_sample_signal
