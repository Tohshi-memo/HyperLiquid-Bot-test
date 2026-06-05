# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T15:52:25.991176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0334` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0415` n `12`; crypto_alt avg `0.2457` n `228`; crypto_major avg `0.3653` n `8`; equity avg `0.0398` n `74`; fx avg `-0.0195` n `6`; index avg `-0.1341` n `23`; metal avg `0.0262` n `18`; unknown avg `-0.2169` n `424`
- 1h: commodity avg `-0.3191` n `12`; crypto_alt avg `-1.7343` n `228`; crypto_major avg `-1.3666` n `8`; equity avg `-1.1989` n `74`; fx avg `-0.0554` n `6`; index avg `-0.3927` n `23`; metal avg `-0.6914` n `18`; unknown avg `-0.5316` n `424`
- 4h: commodity avg `-0.9538` n `12`; crypto_alt avg `-2.5967` n `228`; crypto_major avg `-2.8027` n `8`; equity avg `-3.3244` n `74`; fx avg `-0.2159` n `6`; index avg `-1.7693` n `23`; metal avg `-3.4263` n `18`; unknown avg `-1.0536` n `424`
- 24h: commodity avg `-1.3602` n `12`; crypto_alt avg `-8.9758` n `228`; crypto_major avg `-6.8959` n `8`; equity avg `-4.7341` n `74`; fx avg `-0.0481` n `6`; index avg `-2.3085` n `23`; metal avg `-3.8828` n `18`; unknown avg `-1.3916` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
