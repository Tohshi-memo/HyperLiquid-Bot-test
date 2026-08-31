# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T16:52:27.669667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0588` n `12`; crypto_alt avg `0.1777` n `232`; crypto_major avg `0.3295` n `8`; equity avg `0.0924` n `128`; fx avg `-0.0029` n `6`; index avg `0.0094` n `26`; metal avg `0.0315` n `20`; unknown avg `-0.0452` n `794`
- 1h: commodity avg `-0.0161` n `12`; crypto_alt avg `0.2384` n `232`; crypto_major avg `0.183` n `8`; equity avg `0.1269` n `128`; fx avg `-0.0228` n `6`; index avg `-0.0021` n `26`; metal avg `0.0471` n `20`; unknown avg `-0.1056` n `792`
- 4h: commodity avg `0.0822` n `12`; crypto_alt avg `0.687` n `232`; crypto_major avg `0.9866` n `8`; equity avg `0.4536` n `128`; fx avg `0.0113` n `6`; index avg `-0.0647` n `26`; metal avg `-0.101` n `20`; unknown avg `0.1433` n `790`
- 24h: commodity avg `0.5283` n `12`; crypto_alt avg `-1.4322` n `231`; crypto_major avg `-1.8296` n `8`; equity avg `-0.4673` n `128`; fx avg `-0.1033` n `6`; index avg `-0.2271` n `26`; metal avg `-0.5548` n `20`; unknown avg `-0.0405` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
