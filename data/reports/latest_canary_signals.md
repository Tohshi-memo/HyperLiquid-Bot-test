# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T13:37:26.258744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `0.0173` n `231`; crypto_major avg `0.1218` n `8`; equity avg `0.0223` n `128`; fx avg `-0.0028` n `6`; index avg `0.0149` n `26`; metal avg `-0.0007` n `20`; unknown avg `-0.065` n `793`
- 1h: commodity avg `0.0354` n `12`; crypto_alt avg `0.2193` n `231`; crypto_major avg `0.3441` n `8`; equity avg `0.0117` n `128`; fx avg `-0.0022` n `6`; index avg `0.0095` n `26`; metal avg `0.0161` n `20`; unknown avg `-0.0217` n `793`
- 4h: commodity avg `0.0255` n `12`; crypto_alt avg `1.1546` n `231`; crypto_major avg `0.8328` n `8`; equity avg `0.0055` n `128`; fx avg `-0.0003` n `6`; index avg `0.0272` n `26`; metal avg `0.0117` n `20`; unknown avg `-0.1474` n `789`
- 24h: commodity avg `-0.0173` n `12`; crypto_alt avg `1.7978` n `231`; crypto_major avg `1.3625` n `8`; equity avg `0.2924` n `128`; fx avg `0.0162` n `6`; index avg `0.0951` n `26`; metal avg `0.0845` n `20`; unknown avg `-0.042` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
