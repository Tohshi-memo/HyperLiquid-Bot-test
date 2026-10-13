# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T17:07:31.583280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `13`; crypto_alt avg `-0.3275` n `235`; crypto_major avg `-0.264` n `8`; equity avg `-0.2189` n `151`; fx avg `-0.0039` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.0838` n `1133`
- 1h: commodity avg `0.095` n `13`; crypto_alt avg `-0.0202` n `235`; crypto_major avg `-0.2367` n `8`; equity avg `0.105` n `151`; fx avg `-0.0165` n `6`; index avg `0.0333` n `26`; metal avg `-0.0157` n `20`; unknown avg `-0.057` n `1133`
- 4h: commodity avg `0.6171` n `13`; crypto_alt avg `0.3863` n `235`; crypto_major avg `0.3168` n `8`; equity avg `0.6376` n `151`; fx avg `0.0024` n `6`; index avg `0.0804` n `26`; metal avg `-0.2149` n `20`; unknown avg `0.0774` n `1091`
- 24h: commodity avg `0.4894` n `13`; crypto_alt avg `-1.6224` n `235`; crypto_major avg `-0.4945` n `8`; equity avg `-1.1009` n `151`; fx avg `0.141` n `6`; index avg `-0.2016` n `26`; metal avg `-0.2665` n `20`; unknown avg `0.1974` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1626`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1478`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1234`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0898`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
