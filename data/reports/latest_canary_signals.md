# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T11:52:27.628513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1461` n `12`; crypto_alt avg `0.3288` n `229`; crypto_major avg `0.3966` n `8`; equity avg `0.335` n `91`; fx avg `-0.0053` n `6`; index avg `0.0782` n `25`; metal avg `0.1934` n `20`; unknown avg `0.2423` n `763`
- 1h: commodity avg `-0.0073` n `12`; crypto_alt avg `0.5954` n `229`; crypto_major avg `0.3886` n `8`; equity avg `0.1958` n `91`; fx avg `0.0123` n `6`; index avg `0.0764` n `25`; metal avg `0.0471` n `20`; unknown avg `0.1962` n `763`
- 4h: commodity avg `0.4843` n `12`; crypto_alt avg `-0.3501` n `229`; crypto_major avg `-0.3847` n `8`; equity avg `-1.2835` n `91`; fx avg `0.0334` n `6`; index avg `-0.2418` n `25`; metal avg `-0.9735` n `20`; unknown avg `-0.0127` n `763`
- 24h: commodity avg `1.295` n `12`; crypto_alt avg `-3.4259` n `229`; crypto_major avg `-2.7467` n `8`; equity avg `-2.5172` n `91`; fx avg `-0.1094` n `6`; index avg `-0.5053` n `25`; metal avg `-1.3551` n `20`; unknown avg `-0.8111` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
