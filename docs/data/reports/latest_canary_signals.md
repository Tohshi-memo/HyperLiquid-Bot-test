# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T13:22:28.392486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `13`; crypto_alt avg `-0.1752` n `237`; crypto_major avg `-0.1284` n `8`; equity avg `-0.0551` n `152`; fx avg `-0.0036` n `6`; index avg `-0.0045` n `26`; metal avg `-0.0025` n `20`; unknown avg `-0.0025` n `1230`
- 1h: commodity avg `0.0413` n `13`; crypto_alt avg `-0.2544` n `237`; crypto_major avg `-0.0381` n `8`; equity avg `-0.0937` n `152`; fx avg `-0.0067` n `6`; index avg `-0.0066` n `26`; metal avg `0.006` n `20`; unknown avg `-0.0474` n `1230`
- 4h: commodity avg `0.155` n `13`; crypto_alt avg `0.0235` n `237`; crypto_major avg `0.2497` n `8`; equity avg `0.1501` n `152`; fx avg `-0.0033` n `6`; index avg `0.0078` n `26`; metal avg `0.0055` n `20`; unknown avg `12.6424` n `1218`
- 24h: commodity avg `0.4902` n `13`; crypto_alt avg `-2.7181` n `237`; crypto_major avg `-2.0531` n `8`; equity avg `-0.107` n `152`; fx avg `0.0163` n `6`; index avg `0.0651` n `26`; metal avg `-0.1904` n `20`; unknown avg `194.0681` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
