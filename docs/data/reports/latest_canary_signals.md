# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T13:52:33.623062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.0816` n `228`; crypto_major avg `-0.1291` n `8`; equity avg `-0.0677` n `74`; fx avg `-0.0025` n `6`; index avg `-0.0579` n `23`; metal avg `-0.1745` n `18`; unknown avg `-0.0064` n `644`
- 1h: commodity avg `0.068` n `12`; crypto_alt avg `-0.1567` n `228`; crypto_major avg `-0.0591` n `8`; equity avg `0.0087` n `74`; fx avg `-0.0035` n `6`; index avg `0.032` n `23`; metal avg `-0.2266` n `18`; unknown avg `-0.247` n `644`
- 4h: commodity avg `-0.2298` n `12`; crypto_alt avg `0.3969` n `228`; crypto_major avg `0.7847` n `8`; equity avg `0.183` n `74`; fx avg `-0.0058` n `6`; index avg `0.2177` n `23`; metal avg `-0.0784` n `18`; unknown avg `0.1298` n `643`
- 24h: commodity avg `-1.4751` n `12`; crypto_alt avg `2.2104` n `228`; crypto_major avg `1.1559` n `8`; equity avg `0.8585` n `74`; fx avg `0.0147` n `6`; index avg `1.3615` n `23`; metal avg `1.0325` n `18`; unknown avg `14.4753` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
