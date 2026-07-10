# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T18:07:30.395779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `-0.0316` n `229`; crypto_major avg `-0.0002` n `8`; equity avg `-0.0504` n `92`; fx avg `-0.0071` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0252` n `20`; unknown avg `-0.0137` n `765`
- 1h: commodity avg `0.0063` n `12`; crypto_alt avg `-0.1577` n `229`; crypto_major avg `-0.2087` n `8`; equity avg `0.065` n `92`; fx avg `-0.0291` n `6`; index avg `0.0481` n `25`; metal avg `-0.0069` n `20`; unknown avg `-0.0457` n `765`
- 4h: commodity avg `0.0279` n `12`; crypto_alt avg `-0.2752` n `229`; crypto_major avg `-0.431` n `8`; equity avg `0.1784` n `92`; fx avg `-0.0201` n `6`; index avg `0.0971` n `25`; metal avg `-0.0549` n `20`; unknown avg `-0.103` n `765`
- 24h: commodity avg `-0.2976` n `12`; crypto_alt avg `0.3806` n `229`; crypto_major avg `0.4696` n `8`; equity avg `-0.8892` n `92`; fx avg `-0.1842` n `6`; index avg `0.0124` n `25`; metal avg `-0.1989` n `20`; unknown avg `-0.2442` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
