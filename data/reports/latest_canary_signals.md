# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T01:51:28.909132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.2509` n `228`; crypto_major avg `-0.2334` n `8`; equity avg `-0.3764` n `86`; fx avg `-0.0115` n `6`; index avg `-0.0697` n `23`; metal avg `-0.1208` n `20`; unknown avg `0.0104` n `716`
- 1h: commodity avg `0.0003` n `12`; crypto_alt avg `-0.3349` n `228`; crypto_major avg `-0.4299` n `8`; equity avg `-0.8948` n `86`; fx avg `-0.0395` n `6`; index avg `-0.1769` n `23`; metal avg `-0.4351` n `20`; unknown avg `-0.3916` n `716`
- 4h: commodity avg `-0.0399` n `12`; crypto_alt avg `-0.62` n `228`; crypto_major avg `-0.6269` n `8`; equity avg `-1.553` n `86`; fx avg `0.0221` n `6`; index avg `-0.3498` n `23`; metal avg `-0.4804` n `20`; unknown avg `-0.7428` n `716`
- 24h: commodity avg `-0.543` n `12`; crypto_alt avg `-1.9434` n `228`; crypto_major avg `-1.7742` n `8`; equity avg `-1.7647` n `85`; fx avg `-0.0398` n `6`; index avg `-0.2794` n `23`; metal avg `-0.6272` n `18`; unknown avg `-0.1096` n `647`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
