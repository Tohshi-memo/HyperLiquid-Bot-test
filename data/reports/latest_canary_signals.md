# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T15:07:29.337366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `0.1739` n `234`; crypto_major avg `0.2104` n `8`; equity avg `-0.0073` n `140`; fx avg `0.0008` n `6`; index avg `0.0033` n `26`; metal avg `0.0012` n `20`; unknown avg `0.643` n `940`
- 1h: commodity avg `-0.0602` n `12`; crypto_alt avg `0.1656` n `234`; crypto_major avg `0.2288` n `8`; equity avg `-0.014` n `140`; fx avg `0.0066` n `6`; index avg `0.0009` n `26`; metal avg `0.0157` n `20`; unknown avg `0.6815` n `940`
- 4h: commodity avg `-0.056` n `12`; crypto_alt avg `0.3897` n `234`; crypto_major avg `0.6092` n `8`; equity avg `0.0487` n `140`; fx avg `-0.0127` n `6`; index avg `0.0173` n `26`; metal avg `0.0364` n `20`; unknown avg `0.313` n `932`
- 24h: commodity avg `-0.1836` n `12`; crypto_alt avg `3.2065` n `234`; crypto_major avg `1.7622` n `8`; equity avg `0.748` n `140`; fx avg `0.0238` n `6`; index avg `0.1272` n `26`; metal avg `0.0791` n `20`; unknown avg `1.8398` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
