# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T10:37:24.950300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `0.0472` n `230`; crypto_major avg `0.0265` n `8`; equity avg `0.0446` n `94`; fx avg `-0.0044` n `6`; index avg `0.0027` n `25`; metal avg `0.0196` n `20`; unknown avg `-0.0323` n `768`
- 1h: commodity avg `0.082` n `12`; crypto_alt avg `0.175` n `230`; crypto_major avg `0.1291` n `8`; equity avg `-0.2475` n `94`; fx avg `-0.0094` n `6`; index avg `-0.0597` n `25`; metal avg `-0.0296` n `20`; unknown avg `-0.0071` n `768`
- 4h: commodity avg `0.0833` n `12`; crypto_alt avg `-0.6105` n `230`; crypto_major avg `-0.7833` n `8`; equity avg `-0.6907` n `94`; fx avg `-0.0635` n `6`; index avg `-0.0869` n `25`; metal avg `0.0405` n `20`; unknown avg `-0.2125` n `762`
- 24h: commodity avg `-0.1154` n `12`; crypto_alt avg `-0.631` n `230`; crypto_major avg `-0.6374` n `8`; equity avg `-2.8394` n `93`; fx avg `0.0511` n `6`; index avg `-0.4687` n `25`; metal avg `0.0239` n `20`; unknown avg `-0.0483` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
