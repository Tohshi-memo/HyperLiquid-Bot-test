# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T02:52:24.838052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.36` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0741` n `12`; crypto_alt avg `0.0304` n `228`; crypto_major avg `0.0711` n `8`; equity avg `-0.0241` n `72`; fx avg `0.0256` n `6`; index avg `-0.1082` n `23`; metal avg `0.0082` n `18`; unknown avg `-0.0694` n `420`
- 1h: commodity avg `-0.0529` n `12`; crypto_alt avg `0.1172` n `228`; crypto_major avg `0.0734` n `8`; equity avg `0.0368` n `72`; fx avg `0.0375` n `6`; index avg `0.0224` n `23`; metal avg `0.0766` n `18`; unknown avg `-0.1356` n `419`
- 4h: commodity avg `0.1533` n `12`; crypto_alt avg `1.1023` n `228`; crypto_major avg `0.9022` n `8`; equity avg `-0.164` n `72`; fx avg `0.0511` n `6`; index avg `0.1771` n `23`; metal avg `-0.1866` n `18`; unknown avg `-0.4515` n `419`
- 24h: commodity avg `0.5741` n `12`; crypto_alt avg `-3.6465` n `228`; crypto_major avg `-5.5849` n `8`; equity avg `1.4084` n `72`; fx avg `0.07` n `6`; index avg `1.4264` n `23`; metal avg `0.0837` n `18`; unknown avg `-1.2358` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
