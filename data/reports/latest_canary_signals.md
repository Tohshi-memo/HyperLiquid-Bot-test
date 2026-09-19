# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T19:07:29.457118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `0.1536` n `234`; crypto_major avg `0.1262` n `8`; equity avg `-0.0036` n `140`; fx avg `0.0035` n `6`; index avg `-0.0005` n `26`; metal avg `0.0083` n `20`; unknown avg `1.7794` n `941`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `-0.1124` n `234`; crypto_major avg `-0.0712` n `8`; equity avg `0.0357` n `140`; fx avg `-0.0015` n `6`; index avg `0.0004` n `26`; metal avg `0.0144` n `20`; unknown avg `1.841` n `941`
- 4h: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.1522` n `234`; crypto_major avg `-0.373` n `8`; equity avg `0.0544` n `140`; fx avg `-0.0174` n `6`; index avg `0.0216` n `26`; metal avg `-0.0043` n `20`; unknown avg `7.6549` n `883`
- 24h: commodity avg `0.0987` n `12`; crypto_alt avg `1.935` n `234`; crypto_major avg `0.7629` n `8`; equity avg `0.3485` n `140`; fx avg `0.0162` n `6`; index avg `0.0778` n `26`; metal avg `-0.0294` n `20`; unknown avg `6.9369` n `792`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
