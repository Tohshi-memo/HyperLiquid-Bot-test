# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T18:22:23.579331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2328` n `12`; crypto_alt avg `-0.2706` n `228`; crypto_major avg `-0.3412` n `8`; equity avg `-0.2971` n `66`; fx avg `0.0019` n `5`; index avg `-0.1261` n `23`; metal avg `-0.1284` n `18`; unknown avg `-0.1499` n `384`
- 1h: commodity avg `0.4171` n `12`; crypto_alt avg `-0.6498` n `228`; crypto_major avg `-0.4309` n `8`; equity avg `-0.5105` n `66`; fx avg `-0.031` n `5`; index avg `-0.311` n `23`; metal avg `-0.3458` n `18`; unknown avg `-0.242` n `384`
- 4h: commodity avg `1.1915` n `12`; crypto_alt avg `-0.6611` n `228`; crypto_major avg `-0.6588` n `8`; equity avg `-1.5673` n `66`; fx avg `-0.0604` n `5`; index avg `-0.8044` n `23`; metal avg `-0.1922` n `18`; unknown avg `-0.7829` n `384`
- 24h: commodity avg `1.4308` n `12`; crypto_alt avg `-2.4337` n `228`; crypto_major avg `-2.0978` n `8`; equity avg `-1.4142` n `66`; fx avg `-0.0131` n `5`; index avg `-0.7854` n `23`; metal avg `0.3938` n `18`; unknown avg `-0.5309` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
