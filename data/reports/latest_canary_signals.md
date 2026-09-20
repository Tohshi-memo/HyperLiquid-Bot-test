# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T11:07:32.574488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.2752` n `234`; crypto_major avg `0.0391` n `8`; equity avg `-0.005` n `140`; fx avg `0.0195` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0057` n `20`; unknown avg `-0.0005` n `941`
- 1h: commodity avg `0.0301` n `12`; crypto_alt avg `0.2981` n `234`; crypto_major avg `0.0832` n `8`; equity avg `0.0123` n `140`; fx avg `0.0304` n `6`; index avg `-0.0127` n `26`; metal avg `-0.0194` n `20`; unknown avg `0.2929` n `941`
- 4h: commodity avg `0.0575` n `12`; crypto_alt avg `-0.6407` n `234`; crypto_major avg `-0.2392` n `8`; equity avg `-0.0527` n `140`; fx avg `0.0318` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0081` n `20`; unknown avg `0.5545` n `935`
- 24h: commodity avg `0.2531` n `12`; crypto_alt avg `-2.1093` n `234`; crypto_major avg `-2.2134` n `8`; equity avg `-0.2743` n `140`; fx avg `-0.0387` n `6`; index avg `-0.0538` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.2163` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
