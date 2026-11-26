# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T22:07:27.535678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `13`; crypto_alt avg `-0.1894` n `239`; crypto_major avg `-0.4285` n `8`; equity avg `-0.0652` n `168`; fx avg `0.003` n `6`; index avg `0.0032` n `27`; metal avg `-0.0185` n `20`; unknown avg `1.1778` n `1237`
- 1h: commodity avg `-0.0157` n `13`; crypto_alt avg `-0.0914` n `239`; crypto_major avg `-0.3717` n `8`; equity avg `0.0367` n `168`; fx avg `-0.0018` n `6`; index avg `0.009` n `27`; metal avg `-0.0084` n `20`; unknown avg `3.2687` n `1237`
- 4h: commodity avg `0.0128` n `13`; crypto_alt avg `0.3488` n `239`; crypto_major avg `0.4968` n `8`; equity avg `0.5189` n `168`; fx avg `-0.004` n `6`; index avg `0.047` n `27`; metal avg `0.0449` n `20`; unknown avg `27.2109` n `1163`
- 24h: commodity avg `0.0519` n `13`; crypto_alt avg `1.685` n `239`; crypto_major avg `0.8748` n `8`; equity avg `1.4619` n `168`; fx avg `-0.0141` n `6`; index avg `0.1017` n `27`; metal avg `0.0232` n `20`; unknown avg `14.8036` n `1017`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
