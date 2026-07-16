# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T08:37:29.792172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.3613` n `230`; crypto_major avg `0.5407` n `8`; equity avg `0.1042` n `94`; fx avg `0.0056` n `6`; index avg `0.0462` n `25`; metal avg `0.0026` n `20`; unknown avg `0.2717` n `768`
- 1h: commodity avg `0.0245` n `12`; crypto_alt avg `-0.2922` n `230`; crypto_major avg `-0.2147` n `8`; equity avg `-0.2985` n `94`; fx avg `-0.0175` n `6`; index avg `-0.0203` n `25`; metal avg `0.0564` n `20`; unknown avg `-0.0157` n `768`
- 4h: commodity avg `-0.0343` n `12`; crypto_alt avg `-0.7503` n `230`; crypto_major avg `-0.5561` n `8`; equity avg `-0.6606` n `94`; fx avg `-0.0672` n `6`; index avg `-0.0547` n `25`; metal avg `-0.1166` n `20`; unknown avg `-0.0396` n `752`
- 24h: commodity avg `-0.071` n `12`; crypto_alt avg `-0.4467` n `230`; crypto_major avg `-0.3744` n `8`; equity avg `-2.6824` n `93`; fx avg `0.0333` n `6`; index avg `-0.4446` n `25`; metal avg `-0.0866` n `20`; unknown avg `-0.2105` n `749`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
