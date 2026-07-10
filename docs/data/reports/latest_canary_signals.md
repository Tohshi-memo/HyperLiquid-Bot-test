# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T09:07:27.045115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0188` n `12`; crypto_alt avg `0.044` n `229`; crypto_major avg `0.0192` n `8`; equity avg `-0.1552` n `91`; fx avg `0.0049` n `6`; index avg `0.0023` n `25`; metal avg `0.0218` n `20`; unknown avg `-0.0342` n `765`
- 1h: commodity avg `0.1485` n `12`; crypto_alt avg `0.302` n `229`; crypto_major avg `0.385` n `8`; equity avg `0.0669` n `91`; fx avg `-0.012` n `6`; index avg `0.0233` n `25`; metal avg `-0.0863` n `20`; unknown avg `-0.0039` n `765`
- 4h: commodity avg `-0.1854` n `12`; crypto_alt avg `0.1897` n `229`; crypto_major avg `0.3473` n `8`; equity avg `-0.7467` n `91`; fx avg `-0.0801` n `6`; index avg `-0.1064` n `25`; metal avg `-0.1846` n `20`; unknown avg `1.1408` n `733`
- 24h: commodity avg `-0.8398` n `12`; crypto_alt avg `0.9777` n `229`; crypto_major avg `1.3735` n `8`; equity avg `0.087` n `91`; fx avg `-0.1367` n `6`; index avg `0.1838` n `25`; metal avg `0.073` n `20`; unknown avg `0.0746` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
