# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T02:07:35.808543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0646` n `12`; crypto_alt avg `0.36` n `234`; crypto_major avg `0.1483` n `8`; equity avg `0.0104` n `140`; fx avg `0.0089` n `6`; index avg `0.0069` n `26`; metal avg `-0.0206` n `20`; unknown avg `1.5567` n `941`
- 1h: commodity avg `0.1619` n `12`; crypto_alt avg `0.0942` n `234`; crypto_major avg `-0.1859` n `8`; equity avg `0.0313` n `140`; fx avg `-0.0042` n `6`; index avg `0.0097` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.9985` n `941`
- 4h: commodity avg `0.2499` n `12`; crypto_alt avg `1.2273` n `234`; crypto_major avg `0.1719` n `8`; equity avg `0.0742` n `140`; fx avg `-0.001` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0059` n `20`; unknown avg `1.4167` n `911`
- 24h: commodity avg `0.1572` n `12`; crypto_alt avg `1.1673` n `234`; crypto_major avg `-0.8322` n `8`; equity avg `0.1808` n `140`; fx avg `-0.0522` n `6`; index avg `0.0206` n `26`; metal avg `0.0134` n `20`; unknown avg `0.6668` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
