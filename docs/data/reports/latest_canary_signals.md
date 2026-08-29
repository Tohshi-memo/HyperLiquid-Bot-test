# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T17:07:28.140150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.1641` n `231`; crypto_major avg `-0.1274` n `8`; equity avg `-0.0019` n `128`; fx avg `-0.0005` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.0347` n `792`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.0804` n `231`; crypto_major avg `0.0353` n `8`; equity avg `0.0279` n `128`; fx avg `-0.0062` n `6`; index avg `-0.0027` n `26`; metal avg `0.0067` n `20`; unknown avg `0.0042` n `792`
- 4h: commodity avg `-0.031` n `12`; crypto_alt avg `0.827` n `231`; crypto_major avg `0.8616` n `8`; equity avg `0.0765` n `128`; fx avg `-0.0067` n `6`; index avg `0.0106` n `26`; metal avg `0.0553` n `20`; unknown avg `0.2535` n `778`
- 24h: commodity avg `-0.0351` n `12`; crypto_alt avg `0.5847` n `231`; crypto_major avg `0.3878` n `8`; equity avg `0.2949` n `128`; fx avg `-0.0506` n `6`; index avg `0.0545` n `26`; metal avg `-0.0204` n `20`; unknown avg `0.0409` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2251`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
