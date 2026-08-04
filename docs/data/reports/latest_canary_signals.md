# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T02:22:25.024170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `12`; crypto_alt avg `-0.0459` n `230`; crypto_major avg `-0.0579` n `8`; equity avg `-0.1399` n `107`; fx avg `0.0168` n `6`; index avg `-0.0305` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.0739` n `780`
- 1h: commodity avg `0.0715` n `12`; crypto_alt avg `0.3958` n `230`; crypto_major avg `0.3869` n `8`; equity avg `0.2662` n `107`; fx avg `0.0052` n `6`; index avg `0.0925` n `25`; metal avg `0.1136` n `20`; unknown avg `-0.177` n `780`
- 4h: commodity avg `0.232` n `12`; crypto_alt avg `0.0986` n `230`; crypto_major avg `0.2297` n `8`; equity avg `-0.3224` n `107`; fx avg `-0.0347` n `6`; index avg `-0.0511` n `25`; metal avg `0.1363` n `20`; unknown avg `-0.3189` n `780`
- 24h: commodity avg `0.2033` n `12`; crypto_alt avg `0.8029` n `230`; crypto_major avg `0.7042` n `8`; equity avg `1.2457` n `107`; fx avg `-0.0117` n `6`; index avg `0.0663` n `25`; metal avg `-0.0619` n `20`; unknown avg `0.2309` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
