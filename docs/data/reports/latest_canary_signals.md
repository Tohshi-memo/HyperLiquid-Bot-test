# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T14:07:48.599199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1632` n `12`; crypto_alt avg `0.0237` n `230`; crypto_major avg `-0.0958` n `8`; equity avg `0.1385` n `113`; fx avg `0.0076` n `6`; index avg `0.0264` n `25`; metal avg `-0.0243` n `20`; unknown avg `0.0459` n `787`
- 1h: commodity avg `-0.1756` n `12`; crypto_alt avg `0.0482` n `230`; crypto_major avg `-0.0642` n `8`; equity avg `1.2339` n `113`; fx avg `-0.0044` n `6`; index avg `0.1693` n `25`; metal avg `-0.1361` n `20`; unknown avg `0.0173` n `787`
- 4h: commodity avg `-0.4068` n `12`; crypto_alt avg `0.1119` n `230`; crypto_major avg `0.0166` n `8`; equity avg `1.3871` n `113`; fx avg `-0.032` n `6`; index avg `0.2273` n `25`; metal avg `-0.0393` n `20`; unknown avg `0.1364` n `787`
- 24h: commodity avg `-0.6282` n `12`; crypto_alt avg `-0.2657` n `230`; crypto_major avg `0.3404` n `8`; equity avg `1.7363` n `113`; fx avg `-0.0041` n `6`; index avg `0.2511` n `25`; metal avg `-0.5843` n `20`; unknown avg `0.3496` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2302`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
