# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T00:07:25.986693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.0379` n `229`; crypto_major avg `0.0176` n `8`; equity avg `0.0174` n `92`; fx avg `0.0059` n `6`; index avg `-0.0007` n `25`; metal avg `0.0046` n `20`; unknown avg `-0.0752` n `765`
- 1h: commodity avg `-0.0061` n `12`; crypto_alt avg `0.0065` n `229`; crypto_major avg `0.0859` n `8`; equity avg `0.1044` n `92`; fx avg `0.0129` n `6`; index avg `-0.003` n `25`; metal avg `0.015` n `20`; unknown avg `0.1723` n `765`
- 4h: commodity avg `0.003` n `12`; crypto_alt avg `0.3185` n `229`; crypto_major avg `0.1952` n `8`; equity avg `0.1373` n `92`; fx avg `0.0048` n `6`; index avg `-0.0028` n `25`; metal avg `0.0348` n `20`; unknown avg `-0.313` n `765`
- 24h: commodity avg `-0.2766` n `12`; crypto_alt avg `1.1989` n `229`; crypto_major avg `1.1965` n `8`; equity avg `-0.4357` n `92`; fx avg `-0.1716` n `6`; index avg `0.1007` n `25`; metal avg `0.1811` n `20`; unknown avg `-0.2937` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
