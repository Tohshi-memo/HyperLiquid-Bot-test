# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T11:07:25.208985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `13`; crypto_alt avg `0.062` n `237`; crypto_major avg `0.0697` n `8`; equity avg `0.0176` n `152`; fx avg `-0.0007` n `6`; index avg `0.0015` n `26`; metal avg `0.0033` n `20`; unknown avg `0.1672` n `1228`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `0.0706` n `237`; crypto_major avg `0.1906` n `8`; equity avg `0.0675` n `152`; fx avg `0.0018` n `6`; index avg `0.0035` n `26`; metal avg `0.0008` n `20`; unknown avg `116.5542` n `1228`
- 4h: commodity avg `0.0412` n `13`; crypto_alt avg `-0.5422` n `237`; crypto_major avg `-0.6229` n `8`; equity avg `-0.1864` n `152`; fx avg `0.0093` n `6`; index avg `-0.0255` n `26`; metal avg `-0.0356` n `20`; unknown avg `119.1125` n `1194`
- 24h: commodity avg `0.1827` n `13`; crypto_alt avg `-2.3345` n `237`; crypto_major avg `-1.8634` n `8`; equity avg `-0.5156` n `152`; fx avg `-0.0079` n `6`; index avg `-0.0123` n `26`; metal avg `-0.233` n `20`; unknown avg `193.7045` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.2026`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1982`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
