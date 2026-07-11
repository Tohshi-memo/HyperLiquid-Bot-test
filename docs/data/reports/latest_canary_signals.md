# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T13:22:24.513853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `12`; crypto_alt avg `0.0625` n `230`; crypto_major avg `0.0857` n `8`; equity avg `0.0047` n `92`; fx avg `0.0009` n `6`; index avg `0.0012` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.0048` n `765`
- 1h: commodity avg `-0.0072` n `12`; crypto_alt avg `0.1759` n `230`; crypto_major avg `0.0878` n `8`; equity avg `-0.0718` n `92`; fx avg `-0.0003` n `6`; index avg `-0.0008` n `25`; metal avg `0.0033` n `20`; unknown avg `0.0119` n `765`
- 4h: commodity avg `0.0247` n `12`; crypto_alt avg `0.2925` n `230`; crypto_major avg `0.1621` n `8`; equity avg `-0.0677` n `92`; fx avg `-0.0083` n `6`; index avg `0.0003` n `25`; metal avg `-0.0151` n `20`; unknown avg `-0.2168` n `765`
- 24h: commodity avg `-0.096` n `12`; crypto_alt avg `0.508` n `229`; crypto_major avg `-0.1195` n `8`; equity avg `-0.2578` n `92`; fx avg `-0.0683` n `6`; index avg `0.1515` n `25`; metal avg `0.1405` n `20`; unknown avg `2.9433` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
