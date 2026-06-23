# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T21:52:32.542921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.0546` n `228`; crypto_major avg `-0.0029` n `8`; equity avg `0.0482` n `86`; fx avg `0.0036` n `6`; index avg `0.021` n `23`; metal avg `0.0115` n `20`; unknown avg `-0.1337` n `764`
- 1h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.2241` n `228`; crypto_major avg `0.2799` n `8`; equity avg `0.1868` n `86`; fx avg `-0.0065` n `6`; index avg `0.0676` n `23`; metal avg `0.0866` n `20`; unknown avg `0.2514` n `764`
- 4h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.7985` n `228`; crypto_major avg `0.3015` n `8`; equity avg `-0.2693` n `86`; fx avg `0.0077` n `6`; index avg `0.0057` n `23`; metal avg `-0.091` n `20`; unknown avg `0.9528` n `756`
- 24h: commodity avg `-0.4288` n `12`; crypto_alt avg `-2.3216` n `228`; crypto_major avg `-3.2848` n `8`; equity avg `-3.215` n `86`; fx avg `-0.1437` n `6`; index avg `-0.8844` n `23`; metal avg `-1.1579` n `20`; unknown avg `1.4784` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
