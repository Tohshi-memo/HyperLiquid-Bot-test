# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T07:07:35.488408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0556` n `13`; crypto_alt avg `0.2022` n `237`; crypto_major avg `0.2379` n `8`; equity avg `0.0344` n `152`; fx avg `0.0006` n `6`; index avg `0.0047` n `26`; metal avg `0.0185` n `20`; unknown avg `0.0964` n `1229`
- 1h: commodity avg `0.1156` n `13`; crypto_alt avg `-0.1498` n `237`; crypto_major avg `-0.1069` n `8`; equity avg `-0.0859` n `152`; fx avg `0.009` n `6`; index avg `-0.0111` n `26`; metal avg `0.0113` n `20`; unknown avg `0.6443` n `1229`
- 4h: commodity avg `0.0628` n `13`; crypto_alt avg `-0.6311` n `237`; crypto_major avg `-0.6183` n `8`; equity avg `-0.1415` n `152`; fx avg `0.0056` n `6`; index avg `-0.0021` n `26`; metal avg `0.0047` n `20`; unknown avg `1.4138` n `1195`
- 24h: commodity avg `0.1371` n `13`; crypto_alt avg `-1.6712` n `237`; crypto_major avg `-0.3819` n `8`; equity avg `-0.1405` n `152`; fx avg `-0.0228` n `6`; index avg `-0.007` n `26`; metal avg `-0.0837` n `20`; unknown avg `18.243` n `1054`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
