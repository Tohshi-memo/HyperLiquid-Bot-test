# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T12:07:30.332653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `13`; crypto_alt avg `0.0615` n `237`; crypto_major avg `0.0211` n `8`; equity avg `0.2624` n `152`; fx avg `-0.0003` n `6`; index avg `0.0402` n `26`; metal avg `0.0131` n `20`; unknown avg `10.6004` n `1232`
- 1h: commodity avg `0.0279` n `13`; crypto_alt avg `0.4126` n `237`; crypto_major avg `0.3083` n `8`; equity avg `0.8698` n `152`; fx avg `-0.0027` n `6`; index avg `0.1466` n `26`; metal avg `0.0858` n `20`; unknown avg `12.1219` n `1234`
- 4h: commodity avg `0.0809` n `13`; crypto_alt avg `1.1729` n `237`; crypto_major avg `1.0009` n `8`; equity avg `1.1735` n `152`; fx avg `0.0141` n `6`; index avg `0.1865` n `26`; metal avg `0.0643` n `20`; unknown avg `5.7232` n `1200`
- 24h: commodity avg `-0.3803` n `13`; crypto_alt avg `0.2088` n `237`; crypto_major avg `0.1862` n `8`; equity avg `0.2448` n `152`; fx avg `0.035` n `6`; index avg `0.1133` n `26`; metal avg `0.2003` n `20`; unknown avg `-0.101` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2612`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2271`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2242`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
