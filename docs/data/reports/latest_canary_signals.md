# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T17:22:29.680228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `0.188` n `232`; crypto_major avg `0.2053` n `8`; equity avg `-0.0213` n `128`; fx avg `0.0069` n `6`; index avg `-0.0182` n `26`; metal avg `-0.002` n `20`; unknown avg `-0.0102` n `794`
- 1h: commodity avg `0.0133` n `12`; crypto_alt avg `0.5221` n `232`; crypto_major avg `0.5951` n `8`; equity avg `0.1706` n `128`; fx avg `-0.0036` n `6`; index avg `0.0044` n `26`; metal avg `-0.0153` n `20`; unknown avg `-0.1223` n `792`
- 4h: commodity avg `0.094` n `12`; crypto_alt avg `0.719` n `232`; crypto_major avg `1.0017` n `8`; equity avg `0.3549` n `128`; fx avg `0.0044` n `6`; index avg `-0.0868` n `26`; metal avg `-0.1549` n `20`; unknown avg `0.2703` n `790`
- 24h: commodity avg `0.6086` n `12`; crypto_alt avg `-1.2193` n `231`; crypto_major avg `-1.2858` n `8`; equity avg `-0.494` n `128`; fx avg `-0.1101` n `6`; index avg `-0.2442` n `26`; metal avg `-0.5659` n `20`; unknown avg `0.1615` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
