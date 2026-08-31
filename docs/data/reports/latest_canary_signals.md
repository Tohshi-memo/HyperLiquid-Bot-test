# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T05:52:41.155447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0522` n `12`; crypto_alt avg `0.1674` n `232`; crypto_major avg `0.2724` n `8`; equity avg `0.0202` n `128`; fx avg `-0.0126` n `6`; index avg `0.0054` n `26`; metal avg `0.0195` n `20`; unknown avg `0.2377` n `793`
- 1h: commodity avg `0.0969` n `12`; crypto_alt avg `0.7635` n `232`; crypto_major avg `0.92` n `8`; equity avg `0.4284` n `128`; fx avg `-0.0137` n `6`; index avg `0.048` n `26`; metal avg `0.0909` n `20`; unknown avg `1.1869` n `791`
- 4h: commodity avg `0.1105` n `12`; crypto_alt avg `1.1647` n `231`; crypto_major avg `0.9012` n `8`; equity avg `0.7633` n `128`; fx avg `-0.0263` n `6`; index avg `0.194` n `26`; metal avg `0.0582` n `20`; unknown avg `-0.0606` n `791`
- 24h: commodity avg `0.4807` n `12`; crypto_alt avg `-0.0184` n `231`; crypto_major avg `-1.3547` n `8`; equity avg `-0.6051` n `128`; fx avg `-0.0619` n `6`; index avg `-0.1292` n `26`; metal avg `-0.2756` n `20`; unknown avg `-0.5131` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
