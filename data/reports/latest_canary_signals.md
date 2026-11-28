# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T19:37:28.017020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `13`; crypto_alt avg `-0.1536` n `239`; crypto_major avg `-0.061` n `8`; equity avg `-0.0003` n `168`; fx avg `0.0027` n `6`; index avg `0.0022` n `27`; metal avg `0.0042` n `20`; unknown avg `-0.291` n `1268`
- 1h: commodity avg `0.1329` n `13`; crypto_alt avg `-0.1112` n `239`; crypto_major avg `-0.0884` n `8`; equity avg `0.0838` n `168`; fx avg `0.0034` n `6`; index avg `0.0172` n `27`; metal avg `0.0141` n `20`; unknown avg `1.4357` n `1258`
- 4h: commodity avg `0.0905` n `13`; crypto_alt avg `-0.5028` n `239`; crypto_major avg `-0.0536` n `8`; equity avg `0.1557` n `168`; fx avg `-0.0005` n `6`; index avg `0.017` n `27`; metal avg `0.0242` n `20`; unknown avg `49.9053` n `1213`
- 24h: commodity avg `0.0477` n `13`; crypto_alt avg `-3.4856` n `239`; crypto_major avg `-1.6846` n `8`; equity avg `-0.1215` n `168`; fx avg `-0.0041` n `6`; index avg `-0.0167` n `27`; metal avg `0.1902` n `20`; unknown avg `-0.4487` n `1065`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
