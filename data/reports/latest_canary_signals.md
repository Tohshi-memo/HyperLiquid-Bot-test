# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T00:52:32.943792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.1262` n `229`; crypto_major avg `0.0621` n `8`; equity avg `-0.0077` n `88`; fx avg `0.0022` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0368` n `765`
- 1h: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.1835` n `229`; crypto_major avg `-0.403` n `8`; equity avg `0.0022` n `88`; fx avg `-0.0034` n `6`; index avg `-0.0156` n `25`; metal avg `-0.0183` n `20`; unknown avg `0.2509` n `765`
- 4h: commodity avg `0.0084` n `12`; crypto_alt avg `-0.6101` n `229`; crypto_major avg `-0.5929` n `8`; equity avg `0.0079` n `88`; fx avg `0.0116` n `6`; index avg `0.0063` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.2005` n `765`
- 24h: commodity avg `-0.0322` n `12`; crypto_alt avg `-0.1973` n `229`; crypto_major avg `-0.271` n `8`; equity avg `0.1786` n `88`; fx avg `-0.0184` n `6`; index avg `0.048` n `25`; metal avg `0.094` n `20`; unknown avg `-0.7903` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
