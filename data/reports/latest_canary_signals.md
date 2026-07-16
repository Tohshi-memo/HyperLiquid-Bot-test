# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T06:22:33.464146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.0276` n `230`; crypto_major avg `-0.0773` n `8`; equity avg `0.1742` n `94`; fx avg `-0.005` n `6`; index avg `0.065` n `25`; metal avg `-0.0754` n `20`; unknown avg `-0.0002` n `768`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.1942` n `230`; crypto_major avg `-0.0353` n `8`; equity avg `-0.3251` n `94`; fx avg `0.0041` n `6`; index avg `-0.0718` n `25`; metal avg `-0.0359` n `20`; unknown avg `0.0113` n `752`
- 4h: commodity avg `-0.1073` n `12`; crypto_alt avg `-0.0887` n `230`; crypto_major avg `0.2997` n `8`; equity avg `0.0211` n `94`; fx avg `-0.0141` n `6`; index avg `0.0603` n `25`; metal avg `0.0117` n `20`; unknown avg `-0.1927` n `752`
- 24h: commodity avg `-0.0153` n `12`; crypto_alt avg `-0.0083` n `230`; crypto_major avg `-0.0515` n `8`; equity avg `-2.3245` n `93`; fx avg `0.1331` n `6`; index avg `-0.4291` n `25`; metal avg `0.0715` n `20`; unknown avg `-0.2163` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
