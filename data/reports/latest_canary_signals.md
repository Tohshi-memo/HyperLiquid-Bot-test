# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T17:07:27.432624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0754` n `12`; crypto_alt avg `0.2845` n `229`; crypto_major avg `0.1567` n `8`; equity avg `0.0628` n `91`; fx avg `0.0105` n `6`; index avg `0.0422` n `25`; metal avg `0.0574` n `20`; unknown avg `0.0679` n `764`
- 1h: commodity avg `-0.3306` n `12`; crypto_alt avg `0.6063` n `229`; crypto_major avg `0.5245` n `8`; equity avg `0.7189` n `91`; fx avg `0.0063` n `6`; index avg `0.2237` n `25`; metal avg `0.2913` n `20`; unknown avg `0.1973` n `764`
- 4h: commodity avg `-0.1117` n `12`; crypto_alt avg `0.7845` n `229`; crypto_major avg `0.3952` n `8`; equity avg `1.0874` n `91`; fx avg `0.0765` n `6`; index avg `0.2498` n `25`; metal avg `-0.0892` n `20`; unknown avg `-0.0776` n `764`
- 24h: commodity avg `0.7668` n `12`; crypto_alt avg `-3.435` n `229`; crypto_major avg `-3.775` n `8`; equity avg `-0.3859` n `91`; fx avg `0.0123` n `6`; index avg `-0.184` n `25`; metal avg `-1.2786` n `20`; unknown avg `-0.4283` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
