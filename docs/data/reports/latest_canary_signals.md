# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T23:25:16.996839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.1111` n `232`; crypto_major avg `0.0086` n `8`; equity avg `-0.0305` n `132`; fx avg `-0.0036` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0201` n `20`; unknown avg `0.1011` n `792`
- 1h: commodity avg `-0.021` n `12`; crypto_alt avg `0.0882` n `232`; crypto_major avg `0.2586` n `8`; equity avg `0.0034` n `132`; fx avg `-0.0044` n `6`; index avg `0.0069` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.5475` n `790`
- 4h: commodity avg `0.0767` n `12`; crypto_alt avg `-0.3213` n `232`; crypto_major avg `-0.1779` n `8`; equity avg `-0.2915` n `132`; fx avg `0.0193` n `6`; index avg `0.0002` n `26`; metal avg `-0.0469` n `20`; unknown avg `0.5396` n `772`
- 24h: commodity avg `0.8731` n `12`; crypto_alt avg `-0.6211` n `232`; crypto_major avg `-1.8` n `8`; equity avg `-2.1073` n `130`; fx avg `0.0508` n `6`; index avg `-0.3302` n `26`; metal avg `-0.8691` n `20`; unknown avg `0.1028` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0423`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0391`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0334`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0307`, n `668`, weak_sample_signal
