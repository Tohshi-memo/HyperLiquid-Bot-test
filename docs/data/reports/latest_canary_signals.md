# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T17:37:27.761040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.0291` n `231`; crypto_major avg `0.0073` n `8`; equity avg `-0.0084` n `128`; fx avg `-0.0041` n `6`; index avg `-0.0007` n `26`; metal avg `0.011` n `20`; unknown avg `-0.0195` n `793`
- 1h: commodity avg `0.0193` n `12`; crypto_alt avg `-0.041` n `231`; crypto_major avg `-0.3293` n `8`; equity avg `-0.0027` n `128`; fx avg `0.0055` n `6`; index avg `0.0042` n `26`; metal avg `0.0058` n `20`; unknown avg `0.0975` n `793`
- 4h: commodity avg `0.0321` n `12`; crypto_alt avg `0.3377` n `231`; crypto_major avg `0.3452` n `8`; equity avg `0.1282` n `128`; fx avg `0.0108` n `6`; index avg `0.0086` n `26`; metal avg `0.1091` n `20`; unknown avg `0.3446` n `793`
- 24h: commodity avg `0.0283` n `12`; crypto_alt avg `1.8247` n `231`; crypto_major avg `1.2374` n `8`; equity avg `0.398` n `128`; fx avg `0.0207` n `6`; index avg `0.0956` n `26`; metal avg `0.1358` n `20`; unknown avg `0.1135` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
