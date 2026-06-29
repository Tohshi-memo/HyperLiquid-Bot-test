# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T14:52:30.864575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.64` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0517` n `12`; crypto_alt avg `-0.1403` n `228`; crypto_major avg `-0.0961` n `8`; equity avg `0.1217` n `88`; fx avg `0.003` n `6`; index avg `0.0115` n `23`; metal avg `-0.0426` n `20`; unknown avg `0.2761` n `764`
- 1h: commodity avg `0.0116` n `12`; crypto_alt avg `-0.2551` n `228`; crypto_major avg `-0.2049` n `8`; equity avg `-0.6217` n `88`; fx avg `0.0072` n `6`; index avg `-0.1352` n `23`; metal avg `-0.0362` n `20`; unknown avg `0.6824` n `764`
- 4h: commodity avg `-0.0246` n `12`; crypto_alt avg `-0.4573` n `228`; crypto_major avg `-0.4087` n `8`; equity avg `-0.8689` n `88`; fx avg `0.0491` n `6`; index avg `-0.1694` n `23`; metal avg `-0.0663` n `20`; unknown avg `0.9601` n `764`
- 24h: commodity avg `-0.6071` n `12`; crypto_alt avg `-0.5993` n `228`; crypto_major avg `-0.1784` n `8`; equity avg `-0.3418` n `88`; fx avg `0.1064` n `6`; index avg `-0.1058` n `23`; metal avg `-0.5013` n `20`; unknown avg `0.4734` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
