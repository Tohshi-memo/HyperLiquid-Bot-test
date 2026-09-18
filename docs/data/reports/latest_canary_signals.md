# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T19:07:34.386401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0339` n `12`; crypto_alt avg `0.3449` n `234`; crypto_major avg `0.2184` n `8`; equity avg `0.0734` n `140`; fx avg `-0.0077` n `6`; index avg `0.0148` n `26`; metal avg `-0.0144` n `20`; unknown avg `3.6023` n `938`
- 1h: commodity avg `-0.084` n `12`; crypto_alt avg `0.4512` n `234`; crypto_major avg `0.2277` n `8`; equity avg `0.1466` n `140`; fx avg `0.0035` n `6`; index avg `0.0497` n `26`; metal avg `-0.0847` n `20`; unknown avg `8.2799` n `938`
- 4h: commodity avg `-0.2907` n `12`; crypto_alt avg `1.0574` n `234`; crypto_major avg `0.6223` n `8`; equity avg `0.4516` n `140`; fx avg `-0.0098` n `6`; index avg `0.071` n `26`; metal avg `0.1043` n `20`; unknown avg `6.6264` n `908`
- 24h: commodity avg `-0.1693` n `12`; crypto_alt avg `6.554` n `234`; crypto_major avg `7.0004` n `8`; equity avg `0.878` n `140`; fx avg `0.1939` n `6`; index avg `-0.0515` n `26`; metal avg `0.3265` n `20`; unknown avg `7.7471` n `717`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
