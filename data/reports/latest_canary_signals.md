# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T20:37:31.691389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.2479` n `234`; crypto_major avg `0.1161` n `8`; equity avg `0.0442` n `141`; fx avg `-0.003` n `6`; index avg `0.0073` n `26`; metal avg `-0.0074` n `20`; unknown avg `4.3596` n `932`
- 1h: commodity avg `0.087` n `12`; crypto_alt avg `0.5727` n `234`; crypto_major avg `0.1241` n `8`; equity avg `0.0268` n `141`; fx avg `-0.0001` n `6`; index avg `0.0173` n `26`; metal avg `-0.0405` n `20`; unknown avg `0.0882` n `878`
- 4h: commodity avg `0.1003` n `12`; crypto_alt avg `0.9474` n `234`; crypto_major avg `0.2191` n `8`; equity avg `-0.248` n `141`; fx avg `-0.013` n `6`; index avg `0.0058` n `26`; metal avg `-0.0105` n `20`; unknown avg `-0.0595` n `878`
- 24h: commodity avg `-0.705` n `12`; crypto_alt avg `2.9493` n `234`; crypto_major avg `1.0143` n `8`; equity avg `0.226` n `141`; fx avg `-0.2427` n `6`; index avg `0.2653` n `26`; metal avg `0.1978` n `20`; unknown avg `1148.702` n `794`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
