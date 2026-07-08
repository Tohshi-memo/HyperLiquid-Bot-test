# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T16:52:35.242552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1252` n `12`; crypto_alt avg `0.3428` n `229`; crypto_major avg `0.3401` n `8`; equity avg `0.4116` n `91`; fx avg `-0.022` n `6`; index avg `0.0762` n `25`; metal avg `0.2202` n `20`; unknown avg `0.1519` n `764`
- 1h: commodity avg `-0.4424` n `12`; crypto_alt avg `0.5773` n `229`; crypto_major avg `0.6561` n `8`; equity avg `0.966` n `91`; fx avg `-0.0012` n `6`; index avg `0.241` n `25`; metal avg `0.2795` n `20`; unknown avg `0.2572` n `764`
- 4h: commodity avg `0.1295` n `12`; crypto_alt avg `0.157` n `229`; crypto_major avg `-0.151` n `8`; equity avg `0.8836` n `91`; fx avg `0.0566` n `6`; index avg `0.1686` n `25`; metal avg `-0.2593` n `20`; unknown avg `-0.2471` n `764`
- 24h: commodity avg `0.8779` n `12`; crypto_alt avg `-3.7997` n `229`; crypto_major avg `-4.0697` n `8`; equity avg `-0.3801` n `91`; fx avg `0.0057` n `6`; index avg `-0.2117` n `25`; metal avg `-1.3306` n `20`; unknown avg `-0.5398` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
