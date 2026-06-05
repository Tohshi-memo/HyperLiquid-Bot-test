# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T22:07:22.490831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0167` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0786` n `12`; crypto_alt avg `-1.1488` n `228`; crypto_major avg `-1.1057` n `8`; equity avg `0.0244` n `74`; fx avg `0.005` n `6`; index avg `0.0756` n `23`; metal avg `-0.0144` n `18`; unknown avg `0.6518` n `425`
- 1h: commodity avg `-0.6121` n `12`; crypto_alt avg `-0.5116` n `228`; crypto_major avg `-0.6332` n `8`; equity avg `0.497` n `74`; fx avg `0.0258` n `6`; index avg `0.3835` n `23`; metal avg `0.0779` n `18`; unknown avg `0.9286` n `425`
- 4h: commodity avg `-0.2769` n `12`; crypto_alt avg `-0.2701` n `228`; crypto_major avg `-0.1772` n `8`; equity avg `-0.2954` n `74`; fx avg `0.0069` n `6`; index avg `-0.7777` n `23`; metal avg `-0.4027` n `18`; unknown avg `0.0371` n `424`
- 24h: commodity avg `-1.8505` n `12`; crypto_alt avg `-5.4487` n `228`; crypto_major avg `-5.0353` n `8`; equity avg `-5.8562` n `74`; fx avg `-0.0402` n `6`; index avg `-4.1472` n `23`; metal avg `-4.4129` n `18`; unknown avg `-0.4517` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
