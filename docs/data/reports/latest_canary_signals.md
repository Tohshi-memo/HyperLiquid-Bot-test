# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T04:37:31.583551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.0417` n `228`; crypto_major avg `-0.0366` n `8`; equity avg `-0.0111` n `88`; fx avg `-0.0043` n `6`; index avg `-0.008` n `23`; metal avg `-0.0936` n `20`; unknown avg `-0.1568` n `764`
- 1h: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.3381` n `228`; crypto_major avg `-0.3843` n `8`; equity avg `0.0214` n `88`; fx avg `0.0017` n `6`; index avg `0.017` n `23`; metal avg `-0.1858` n `20`; unknown avg `-0.061` n `764`
- 4h: commodity avg `0.0398` n `12`; crypto_alt avg `1.4345` n `228`; crypto_major avg `1.2556` n `8`; equity avg `0.4526` n `88`; fx avg `0.0628` n `6`; index avg `0.071` n `23`; metal avg `0.032` n `20`; unknown avg `0.3764` n `764`
- 24h: commodity avg `-0.2509` n `12`; crypto_alt avg `-0.0402` n `228`; crypto_major avg `-0.0266` n `8`; equity avg `-0.0343` n `88`; fx avg `0.0468` n `6`; index avg `-0.0967` n `23`; metal avg `-0.3096` n `20`; unknown avg `-0.7357` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
