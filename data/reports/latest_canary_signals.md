# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T08:07:29.594178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0865` n `12`; crypto_alt avg `0.1128` n `229`; crypto_major avg `-0.0085` n `8`; equity avg `-0.0681` n `91`; fx avg `0.0366` n `6`; index avg `-0.0217` n `25`; metal avg `-0.0548` n `20`; unknown avg `0.0468` n `763`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `0.1276` n `229`; crypto_major avg `0.2095` n `8`; equity avg `0.2549` n `91`; fx avg `0.0353` n `6`; index avg `0.0127` n `25`; metal avg `-0.0591` n `20`; unknown avg `-0.0285` n `763`
- 4h: commodity avg `0.0428` n `12`; crypto_alt avg `-0.0582` n `229`; crypto_major avg `-0.1144` n `8`; equity avg `-0.4869` n `91`; fx avg `-0.0359` n `6`; index avg `-0.1986` n `25`; metal avg `-0.1109` n `20`; unknown avg `-0.1773` n `743`
- 24h: commodity avg `0.7418` n `12`; crypto_alt avg `-2.564` n `229`; crypto_major avg `-1.9824` n `8`; equity avg `-1.6095` n `91`; fx avg `-0.1865` n `6`; index avg `-0.3679` n `25`; metal avg `-0.1659` n `20`; unknown avg `-0.5814` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
