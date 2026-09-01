# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T23:52:24.543471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `0.0328` n `232`; crypto_major avg `-0.0943` n `8`; equity avg `0.0074` n `132`; fx avg `-0.0124` n `6`; index avg `0.0151` n `26`; metal avg `-0.0011` n `20`; unknown avg `-0.1315` n `792`
- 1h: commodity avg `-0.021` n `12`; crypto_alt avg `0.248` n `232`; crypto_major avg `0.2687` n `8`; equity avg `0.004` n `132`; fx avg `-0.0246` n `6`; index avg `0.0136` n `26`; metal avg `0.0232` n `20`; unknown avg `-0.1918` n `790`
- 4h: commodity avg `0.0483` n `12`; crypto_alt avg `0.0083` n `232`; crypto_major avg `0.181` n `8`; equity avg `-0.1498` n `132`; fx avg `-0.01` n `6`; index avg `0.0259` n `26`; metal avg `0.0473` n `20`; unknown avg `-0.3495` n `772`
- 24h: commodity avg `0.87` n `12`; crypto_alt avg `-0.2261` n `232`; crypto_major avg `-1.5365` n `8`; equity avg `-2.1204` n `130`; fx avg `0.0326` n `6`; index avg `-0.3527` n `26`; metal avg `-0.8758` n `20`; unknown avg `-0.3742` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0424`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0399`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0317`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0312`, n `668`, weak_sample_signal
