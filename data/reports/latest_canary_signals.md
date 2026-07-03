# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T03:22:28.179494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0407` n `12`; crypto_alt avg `0.0669` n `229`; crypto_major avg `0.185` n `8`; equity avg `0.0506` n `88`; fx avg `0.0234` n `6`; index avg `0.0264` n `25`; metal avg `-0.0056` n `20`; unknown avg `-0.0927` n `765`
- 1h: commodity avg `0.0372` n `12`; crypto_alt avg `-0.1395` n `229`; crypto_major avg `-0.1907` n `8`; equity avg `0.0113` n `88`; fx avg `0.062` n `6`; index avg `0.0179` n `25`; metal avg `0.0023` n `20`; unknown avg `0.0651` n `761`
- 4h: commodity avg `0.1811` n `12`; crypto_alt avg `0.654` n `229`; crypto_major avg `0.4195` n `8`; equity avg `1.1183` n `88`; fx avg `0.1115` n `6`; index avg `0.2234` n `25`; metal avg `0.6459` n `20`; unknown avg `0.6249` n `761`
- 24h: commodity avg `0.4245` n `12`; crypto_alt avg `2.2571` n `228`; crypto_major avg `3.2038` n `8`; equity avg `-1.111` n `88`; fx avg `-0.0357` n `6`; index avg `-0.2053` n `25`; metal avg `1.227` n `20`; unknown avg `6.2313` n `735`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
