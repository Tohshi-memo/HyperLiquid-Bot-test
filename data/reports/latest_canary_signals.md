# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T18:52:27.637634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.2452` n `229`; crypto_major avg `-0.2254` n `8`; equity avg `-0.0516` n `92`; fx avg `0.002` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0258` n `20`; unknown avg `-0.0841` n `765`
- 1h: commodity avg `0.1678` n `12`; crypto_alt avg `-0.3089` n `229`; crypto_major avg `-0.2733` n `8`; equity avg `-0.1901` n `92`; fx avg `-0.0159` n `6`; index avg `-0.0167` n `25`; metal avg `-0.0381` n `20`; unknown avg `-0.0832` n `765`
- 4h: commodity avg `0.0728` n `12`; crypto_alt avg `0.0116` n `229`; crypto_major avg `-0.2184` n `8`; equity avg `0.3169` n `92`; fx avg `-0.0545` n `6`; index avg `0.0941` n `25`; metal avg `-0.0555` n `20`; unknown avg `-0.1592` n `765`
- 24h: commodity avg `-0.2074` n `12`; crypto_alt avg `0.1989` n `229`; crypto_major avg `0.4883` n `8`; equity avg `-0.9112` n `92`; fx avg `-0.1652` n `6`; index avg `0.0205` n `25`; metal avg `-0.1059` n `20`; unknown avg `-0.1941` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
