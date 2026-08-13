# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T16:22:28.955880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0353` n `12`; crypto_alt avg `0.1116` n `230`; crypto_major avg `0.1957` n `8`; equity avg `0.0876` n `113`; fx avg `0.0005` n `6`; index avg `0.0076` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.0584` n `787`
- 1h: commodity avg `0.0581` n `12`; crypto_alt avg `-0.6028` n `230`; crypto_major avg `-0.429` n `8`; equity avg `-0.3289` n `113`; fx avg `-0.0038` n `6`; index avg `-0.0613` n `25`; metal avg `-0.0656` n `20`; unknown avg `-0.1275` n `787`
- 4h: commodity avg `0.066` n `12`; crypto_alt avg `-0.2361` n `230`; crypto_major avg `0.0674` n `8`; equity avg `1.4679` n `113`; fx avg `-0.0154` n `6`; index avg `0.2563` n `25`; metal avg `-0.2475` n `20`; unknown avg `-0.0569` n `787`
- 24h: commodity avg `-0.246` n `12`; crypto_alt avg `-0.4955` n `230`; crypto_major avg `0.0661` n `8`; equity avg `1.2961` n `113`; fx avg `0.0032` n `6`; index avg `0.3035` n `25`; metal avg `-0.6144` n `20`; unknown avg `0.1446` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2301`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
