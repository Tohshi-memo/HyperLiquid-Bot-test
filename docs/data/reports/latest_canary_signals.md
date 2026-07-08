# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T17:22:37.392313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0443` n `12`; crypto_alt avg `0.1771` n `229`; crypto_major avg `0.3081` n `8`; equity avg `0.1661` n `91`; fx avg `0.0001` n `6`; index avg `0.0233` n `25`; metal avg `0.0375` n `20`; unknown avg `0.0561` n `764`
- 1h: commodity avg `-0.2824` n `12`; crypto_alt avg `0.5857` n `229`; crypto_major avg `0.6015` n `8`; equity avg `0.4069` n `91`; fx avg `0.0087` n `6`; index avg `0.0969` n `25`; metal avg `0.2868` n `20`; unknown avg `0.1501` n `764`
- 4h: commodity avg `-0.0976` n `12`; crypto_alt avg `0.7238` n `229`; crypto_major avg `0.5188` n `8`; equity avg `1.111` n `91`; fx avg `0.0703` n `6`; index avg `0.2662` n `25`; metal avg `-0.0901` n `20`; unknown avg `-0.0308` n `764`
- 24h: commodity avg `0.6906` n `12`; crypto_alt avg `-3.1876` n `229`; crypto_major avg `-3.4639` n `8`; equity avg `-0.2306` n `91`; fx avg `0.0165` n `6`; index avg `-0.184` n `25`; metal avg `-1.2098` n `20`; unknown avg `-0.4305` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
