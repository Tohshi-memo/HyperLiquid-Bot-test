# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T18:22:37.780795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `-0.055` n `230`; crypto_major avg `0.0193` n `8`; equity avg `0.0749` n `113`; fx avg `0.0029` n `6`; index avg `0.0023` n `25`; metal avg `0.0165` n `20`; unknown avg `0.0311` n `787`
- 1h: commodity avg `-0.1179` n `12`; crypto_alt avg `0.0251` n `230`; crypto_major avg `0.0509` n `8`; equity avg `-0.1653` n `113`; fx avg `0.0042` n `6`; index avg `-0.0442` n `25`; metal avg `-0.0429` n `20`; unknown avg `-0.049` n `787`
- 4h: commodity avg `0.1128` n `12`; crypto_alt avg `-0.7126` n `230`; crypto_major avg `-0.4267` n `8`; equity avg `-0.0263` n `113`; fx avg `0.0061` n `6`; index avg `0.031` n `25`; metal avg `-0.0088` n `20`; unknown avg `-0.1133` n `787`
- 24h: commodity avg `-0.4935` n `12`; crypto_alt avg `-0.6748` n `230`; crypto_major avg `-0.0654` n `8`; equity avg `1.2365` n `113`; fx avg `-0.0047` n `6`; index avg `0.3043` n `25`; metal avg `-0.45` n `20`; unknown avg `0.0504` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.233`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
