# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T16:07:29.105936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1884` n `12`; crypto_alt avg `0.2559` n `229`; crypto_major avg `0.2879` n `8`; equity avg `0.3082` n `91`; fx avg `0.0031` n `6`; index avg `0.0595` n `25`; metal avg `0.0455` n `20`; unknown avg `0.1136` n `764`
- 1h: commodity avg `-0.1097` n `12`; crypto_alt avg `0.0683` n `229`; crypto_major avg `0.1234` n `8`; equity avg `-0.2053` n `91`; fx avg `0.004` n `6`; index avg `-0.0304` n `25`; metal avg `-0.0997` n `20`; unknown avg `-0.0485` n `764`
- 4h: commodity avg `0.2314` n `12`; crypto_alt avg `-0.5203` n `229`; crypto_major avg `-0.9018` n `8`; equity avg `0.3236` n `91`; fx avg `0.0573` n `6`; index avg `0.0429` n `25`; metal avg `-0.3916` n `20`; unknown avg `-0.2394` n `757`
- 24h: commodity avg `1.1124` n `12`; crypto_alt avg `-3.8474` n `229`; crypto_major avg `-4.0625` n `8`; equity avg `-0.5846` n `91`; fx avg `0.0005` n `6`; index avg `-0.3139` n `25`; metal avg `-1.4792` n `20`; unknown avg `-0.6314` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
