# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T23:26:01.989926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `0.0963` n `229`; crypto_major avg `0.1469` n `8`; equity avg `0.0524` n `92`; fx avg `0.0084` n `6`; index avg `-0.0027` n `25`; metal avg `0.0071` n `20`; unknown avg `0.2697` n `765`
- 1h: commodity avg `0.0039` n `12`; crypto_alt avg `0.0689` n `229`; crypto_major avg `0.1276` n `8`; equity avg `0.0452` n `92`; fx avg `0.0028` n `6`; index avg `-0.0146` n `25`; metal avg `-0.003` n `20`; unknown avg `0.2751` n `765`
- 4h: commodity avg `-0.0363` n `12`; crypto_alt avg `0.629` n `229`; crypto_major avg `0.4809` n `8`; equity avg `0.0056` n `92`; fx avg `-0.0056` n `6`; index avg `0.0002` n `25`; metal avg `0.0932` n `20`; unknown avg `-0.1589` n `765`
- 24h: commodity avg `-0.2443` n `12`; crypto_alt avg `1.3096` n `229`; crypto_major avg `1.2207` n `8`; equity avg `-0.7559` n `92`; fx avg `-0.1664` n `6`; index avg `0.0151` n `25`; metal avg `0.1336` n `20`; unknown avg `-0.2167` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
