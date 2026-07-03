# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T18:07:27.805555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.1002` n `229`; crypto_major avg `0.0156` n `8`; equity avg `0.0706` n `88`; fx avg `0.0032` n `6`; index avg `-0.0021` n `25`; metal avg `0.0023` n `20`; unknown avg `0.7313` n `765`
- 1h: commodity avg `-0.0282` n `12`; crypto_alt avg `-0.0723` n `229`; crypto_major avg `0.0687` n `8`; equity avg `0.0674` n `88`; fx avg `0.0016` n `6`; index avg `0.0231` n `25`; metal avg `0.0049` n `20`; unknown avg `1.7484` n `765`
- 4h: commodity avg `-0.1077` n `12`; crypto_alt avg `0.2241` n `229`; crypto_major avg `0.3697` n `8`; equity avg `0.2061` n `88`; fx avg `-0.0144` n `6`; index avg `0.0411` n `25`; metal avg `0.0485` n `20`; unknown avg `2.6169` n `765`
- 24h: commodity avg `0.2358` n `12`; crypto_alt avg `2.4776` n `229`; crypto_major avg `2.1739` n `8`; equity avg `2.3866` n `88`; fx avg `-0.038` n `6`; index avg `0.6699` n `25`; metal avg `0.6318` n `20`; unknown avg `11.1146` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
