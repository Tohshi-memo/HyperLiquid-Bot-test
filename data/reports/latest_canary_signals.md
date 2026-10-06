# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T06:37:27.100478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `13`; crypto_alt avg `0.2781` n `235`; crypto_major avg `0.1407` n `8`; equity avg `0.0316` n `149`; fx avg `0.0032` n `6`; index avg `0.0011` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.1036` n `1074`
- 1h: commodity avg `-0.2471` n `13`; crypto_alt avg `-0.2455` n `235`; crypto_major avg `-0.3688` n `8`; equity avg `0.0593` n `149`; fx avg `0.0011` n `6`; index avg `0.0235` n `26`; metal avg `0.0209` n `20`; unknown avg `4.4418` n `1044`
- 4h: commodity avg `-0.2452` n `13`; crypto_alt avg `-0.0078` n `235`; crypto_major avg `-0.3467` n `8`; equity avg `0.2106` n `149`; fx avg `0.0067` n `6`; index avg `0.0555` n `26`; metal avg `-0.013` n `20`; unknown avg `4.9571` n `1036`
- 24h: commodity avg `-0.2767` n `13`; crypto_alt avg `-0.8774` n `235`; crypto_major avg `-0.5575` n `8`; equity avg `0.2399` n `149`; fx avg `0.0745` n `6`; index avg `0.1634` n `26`; metal avg `-0.1243` n `20`; unknown avg `587.3036` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
