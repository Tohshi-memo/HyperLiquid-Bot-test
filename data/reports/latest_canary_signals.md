# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T17:22:19.335206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.07` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.5796` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.9212` n `12`; crypto_alt avg `0.8461` n `228`; crypto_major avg `0.8438` n `8`; equity avg `0.703` n `67`; fx avg `-0.0107` n `6`; index avg `0.3743` n `23`; metal avg `0.6396` n `18`; unknown avg `0.3802` n `385`
- 1h: commodity avg `-1.1184` n `12`; crypto_alt avg `0.9112` n `228`; crypto_major avg `0.721` n `8`; equity avg `0.8528` n `67`; fx avg `-0.0114` n `6`; index avg `0.3981` n `23`; metal avg `0.6255` n `18`; unknown avg `0.2797` n `385`
- 4h: commodity avg `-1.5811` n `12`; crypto_alt avg `1.3336` n `228`; crypto_major avg `0.9985` n `8`; equity avg `1.406` n `67`; fx avg `-0.0361` n `6`; index avg `0.4599` n `23`; metal avg `1.4766` n `18`; unknown avg `1.6878` n `385`
- 24h: commodity avg `-0.0922` n `12`; crypto_alt avg `1.6235` n `228`; crypto_major avg `2.3331` n `8`; equity avg `1.818` n `66`; fx avg `-0.0021` n `6`; index avg `0.5701` n `23`; metal avg `0.4482` n `18`; unknown avg `7.2496` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
