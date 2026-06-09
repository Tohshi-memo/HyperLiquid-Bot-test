# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T10:22:31.116637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2562` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `-0.0275` n `228`; crypto_major avg `-0.041` n `8`; equity avg `-0.0395` n `74`; fx avg `0.0218` n `6`; index avg `-0.0214` n `23`; metal avg `0.1871` n `18`; unknown avg `0.5498` n `547`
- 1h: commodity avg `0.2387` n `12`; crypto_alt avg `-0.5935` n `228`; crypto_major avg `-0.6677` n `8`; equity avg `-0.121` n `74`; fx avg `0.0621` n `6`; index avg `-0.0296` n `23`; metal avg `0.1018` n `18`; unknown avg `0.7283` n `547`
- 4h: commodity avg `0.1257` n `12`; crypto_alt avg `-1.0616` n `228`; crypto_major avg `-1.1303` n `8`; equity avg `-0.2672` n `74`; fx avg `0.2092` n `6`; index avg `0.1259` n `23`; metal avg `0.1583` n `18`; unknown avg `0.0351` n `547`
- 24h: commodity avg `-1.3052` n `12`; crypto_alt avg `-0.5603` n `228`; crypto_major avg `0.1225` n `8`; equity avg `2.3163` n `74`; fx avg `0.1006` n `6`; index avg `1.1991` n `23`; metal avg `1.1793` n `18`; unknown avg `-2.737` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
