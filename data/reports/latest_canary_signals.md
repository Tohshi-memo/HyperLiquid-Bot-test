# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T16:07:29.546168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.35` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.7913` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0265` n `12`; crypto_alt avg `0.035` n `230`; crypto_major avg `-0.0172` n `8`; equity avg `0.1949` n `113`; fx avg `-0.0009` n `6`; index avg `0.0111` n `25`; metal avg `0.0323` n `20`; unknown avg `0.056` n `786`
- 1h: commodity avg `-0.018` n `12`; crypto_alt avg `-0.0326` n `230`; crypto_major avg `0.1715` n `8`; equity avg `0.2145` n `113`; fx avg `0.0032` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0461` n `20`; unknown avg `-0.0006` n `786`
- 4h: commodity avg `-0.0923` n `12`; crypto_alt avg `-0.5906` n `230`; crypto_major avg `-0.7893` n `8`; equity avg `1.002` n `113`; fx avg `-0.0209` n `6`; index avg `0.0743` n `25`; metal avg `-0.114` n `20`; unknown avg `0.24` n `786`
- 24h: commodity avg `0.1454` n `12`; crypto_alt avg `0.062` n `230`; crypto_major avg `1.0979` n `8`; equity avg `3.4637` n `113`; fx avg `0.0362` n `6`; index avg `0.3404` n `25`; metal avg `0.2673` n `20`; unknown avg `0.0924` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2271`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2048`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
