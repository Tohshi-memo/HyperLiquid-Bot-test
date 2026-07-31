# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T21:22:30.506757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0712` n `12`; crypto_alt avg `0.0613` n `230`; crypto_major avg `0.056` n `8`; equity avg `-0.0995` n `102`; fx avg `0.0209` n `6`; index avg `0.0485` n `25`; metal avg `-0.0037` n `20`; unknown avg `1.6452` n `781`
- 1h: commodity avg `0.5182` n `12`; crypto_alt avg `-0.1005` n `230`; crypto_major avg `-0.0119` n `8`; equity avg `-0.186` n `102`; fx avg `-0.048` n `6`; index avg `-0.0199` n `25`; metal avg `-0.0481` n `20`; unknown avg `2.6693` n `780`
- 4h: commodity avg `0.5809` n `12`; crypto_alt avg `-0.1895` n `230`; crypto_major avg `-0.1717` n `8`; equity avg `-0.5691` n `102`; fx avg `-0.0786` n `6`; index avg `-0.0684` n `25`; metal avg `0.0083` n `20`; unknown avg `7.5677` n `780`
- 24h: commodity avg `0.694` n `12`; crypto_alt avg `-0.5366` n `230`; crypto_major avg `-2.0425` n `8`; equity avg `-1.2528` n `102`; fx avg `0.1173` n `6`; index avg `0.0985` n `25`; metal avg `-0.4351` n `20`; unknown avg `0.2161` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
