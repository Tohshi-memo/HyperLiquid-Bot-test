# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T05:07:30.021902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0309` n `12`; crypto_alt avg `-0.2996` n `228`; crypto_major avg `-0.2914` n `8`; equity avg `-0.1418` n `74`; fx avg `-0.022` n `6`; index avg `-0.0522` n `23`; metal avg `-0.2037` n `18`; unknown avg `0.3321` n `550`
- 1h: commodity avg `-0.3765` n `12`; crypto_alt avg `0.2914` n `228`; crypto_major avg `-0.0776` n `8`; equity avg `0.0592` n `74`; fx avg `0.0012` n `6`; index avg `0.0433` n `23`; metal avg `0.0903` n `18`; unknown avg `15.0018` n `550`
- 4h: commodity avg `-0.4455` n `12`; crypto_alt avg `1.592` n `228`; crypto_major avg `1.1147` n `8`; equity avg `0.1686` n `74`; fx avg `0.0036` n `6`; index avg `0.2722` n `23`; metal avg `0.3491` n `18`; unknown avg `2.665` n `550`
- 24h: commodity avg `1.5337` n `12`; crypto_alt avg `1.4765` n `228`; crypto_major avg `0.7233` n `8`; equity avg `-0.1476` n `74`; fx avg `0.0121` n `6`; index avg `-0.4742` n `23`; metal avg `-0.3049` n `18`; unknown avg `2.8252` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
