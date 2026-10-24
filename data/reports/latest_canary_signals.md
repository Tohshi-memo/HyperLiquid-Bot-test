# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T12:52:25.769983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `13`; crypto_alt avg `0.1112` n `237`; crypto_major avg `0.0199` n `8`; equity avg `-0.0146` n `152`; fx avg `0.0006` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0046` n `20`; unknown avg `-0.0064` n `1230`
- 1h: commodity avg `0.0382` n `13`; crypto_alt avg `0.257` n `237`; crypto_major avg `0.214` n `8`; equity avg `0.1335` n `152`; fx avg `0.0043` n `6`; index avg `0.0266` n `26`; metal avg `0.0117` n `20`; unknown avg `0.11` n `1224`
- 4h: commodity avg `0.1347` n `13`; crypto_alt avg `0.2984` n `237`; crypto_major avg `0.1374` n `8`; equity avg `0.1294` n `152`; fx avg `-0.0009` n `6`; index avg `0.0062` n `26`; metal avg `-0.0178` n `20`; unknown avg `6.718` n `1206`
- 24h: commodity avg `0.3798` n `13`; crypto_alt avg `-2.4595` n `237`; crypto_major avg `-1.8079` n `8`; equity avg `0.0904` n `152`; fx avg `0.0112` n `6`; index avg `0.0849` n `26`; metal avg `-0.1822` n `20`; unknown avg `193.8356` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1953`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
