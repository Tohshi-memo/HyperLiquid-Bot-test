# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T23:37:25.363167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `0.0269` n `229`; crypto_major avg `0.0297` n `8`; equity avg `-0.0065` n `88`; fx avg `-0.006` n `6`; index avg `0.0035` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.23` n `765`
- 1h: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.249` n `229`; crypto_major avg `-0.2337` n `8`; equity avg `-0.0124` n `88`; fx avg `-0.0` n `6`; index avg `0.0063` n `25`; metal avg `0.0099` n `20`; unknown avg `-0.1938` n `765`
- 4h: commodity avg `0.0316` n `12`; crypto_alt avg `-0.684` n `229`; crypto_major avg `-0.4099` n `8`; equity avg `0.0154` n `88`; fx avg `0.0208` n `6`; index avg `0.0369` n `25`; metal avg `0.0122` n `20`; unknown avg `-0.2429` n `765`
- 24h: commodity avg `0.0267` n `12`; crypto_alt avg `-0.1116` n `229`; crypto_major avg `0.2664` n `8`; equity avg `0.2509` n `88`; fx avg `-0.0082` n `6`; index avg `0.0243` n `25`; metal avg `0.0696` n `20`; unknown avg `-0.7207` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
