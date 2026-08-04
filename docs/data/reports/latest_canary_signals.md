# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T06:07:35.137866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.0867` n `230`; crypto_major avg `0.0324` n `8`; equity avg `0.1909` n `107`; fx avg `0.0112` n `6`; index avg `0.0136` n `25`; metal avg `0.0362` n `20`; unknown avg `0.005` n `765`
- 1h: commodity avg `-0.0507` n `12`; crypto_alt avg `0.0058` n `230`; crypto_major avg `-0.0935` n `8`; equity avg `0.6962` n `107`; fx avg `0.0351` n `6`; index avg `0.1344` n `25`; metal avg `0.0656` n `20`; unknown avg `-0.0377` n `765`
- 4h: commodity avg `0.0313` n `12`; crypto_alt avg `-0.0086` n `230`; crypto_major avg `0.0037` n `8`; equity avg `0.7096` n `107`; fx avg `0.1083` n `6`; index avg `0.0914` n `25`; metal avg `0.175` n `20`; unknown avg `-0.0278` n `764`
- 24h: commodity avg `0.2869` n `12`; crypto_alt avg `1.0494` n `230`; crypto_major avg `1.0701` n `8`; equity avg `2.3828` n `107`; fx avg `0.1088` n `6`; index avg `0.2608` n `25`; metal avg `0.0421` n `20`; unknown avg `0.1493` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
