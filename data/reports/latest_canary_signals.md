# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T12:30:24.623449+00:00`
- Correlation status: `ready`
- Asset price records: `360`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0743` n `7`; crypto_alt avg `0.1281` n `223`; crypto_major avg `0.0698` n `7`; equity avg `0.0201` n `47`; fx avg `0.0096` n `4`; index avg `0.0233` n `6`; metal avg `0.0072` n `7`; unknown avg `0.2255` n `312`
- 1h: commodity avg `-0.5118` n `7`; crypto_alt avg `0.2841` n `223`; crypto_major avg `0.3538` n `7`; equity avg `0.3029` n `47`; fx avg `0.0114` n `4`; index avg `0.242` n `6`; metal avg `0.4545` n `7`; unknown avg `0.2013` n `312`
- 4h: commodity avg `-0.2287` n `7`; crypto_alt avg `0.3277` n `223`; crypto_major avg `0.5952` n `7`; equity avg `0.3578` n `47`; fx avg `0.0694` n `4`; index avg `0.1115` n `6`; metal avg `0.5826` n `7`; unknown avg `0.2516` n `312`
- 24h: commodity avg `0.2643` n `7`; crypto_alt avg `2.3192` n `223`; crypto_major avg `2.2491` n `7`; equity avg `0.8007` n `47`; fx avg `0.0779` n `4`; index avg `0.4716` n `6`; metal avg `0.6601` n `7`; unknown avg `-0.2263` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2089`, n `356`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2016`, n `356`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1354`, n `356`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `356`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `356`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `356`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `356`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `356`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `352`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `356`, weak_sample_signal
