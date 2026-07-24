# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T00:52:28.723182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.097` n `230`; crypto_major avg `0.0389` n `8`; equity avg `0.1623` n `100`; fx avg `-0.0172` n `6`; index avg `0.0489` n `25`; metal avg `0.004` n `20`; unknown avg `0.0648` n `772`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.2191` n `230`; crypto_major avg `-0.172` n `8`; equity avg `-0.2511` n `100`; fx avg `-0.0527` n `6`; index avg `-0.0994` n `25`; metal avg `0.0165` n `20`; unknown avg `0.3673` n `772`
- 4h: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.6575` n `230`; crypto_major avg `-0.4963` n `8`; equity avg `-0.6639` n `100`; fx avg `-0.0643` n `6`; index avg `-0.1414` n `25`; metal avg `-0.0004` n `20`; unknown avg `-0.0695` n `772`
- 24h: commodity avg `0.6441` n `12`; crypto_alt avg `-2.1363` n `230`; crypto_major avg `-2.6692` n `8`; equity avg `-2.0302` n `99`; fx avg `-0.0893` n `6`; index avg `-0.4866` n `25`; metal avg `-0.763` n `20`; unknown avg `-0.4037` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0855`, n `666`, weak_sample_signal
