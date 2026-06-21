# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T18:37:29.837351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.1804` n `228`; crypto_major avg `0.3076` n `8`; equity avg `0.0182` n `78`; fx avg `-0.0005` n `6`; index avg `0.0057` n `23`; metal avg `0.0108` n `18`; unknown avg `0.5107` n `702`
- 1h: commodity avg `0.0503` n `12`; crypto_alt avg `0.0175` n `228`; crypto_major avg `0.2323` n `8`; equity avg `-0.0204` n `78`; fx avg `-0.0017` n `6`; index avg `-0.0199` n `23`; metal avg `-0.0673` n `18`; unknown avg `0.134` n `702`
- 4h: commodity avg `0.1589` n `12`; crypto_alt avg `0.0258` n `228`; crypto_major avg `0.2516` n `8`; equity avg `0.0187` n `78`; fx avg `-0.0954` n `6`; index avg `-0.0389` n `23`; metal avg `-0.0579` n `18`; unknown avg `-0.4491` n `702`
- 24h: commodity avg `0.2052` n `12`; crypto_alt avg `1.539` n `228`; crypto_major avg `0.4416` n `8`; equity avg `0.4111` n `78`; fx avg `-0.0694` n `6`; index avg `0.0065` n `23`; metal avg `-0.0929` n `18`; unknown avg `-0.1223` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
