# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T09:22:17.363081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.314` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.2897` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `0.1026` n `228`; crypto_major avg `0.0628` n `8`; equity avg `0.0197` n `65`; fx avg `-0.0009` n `5`; index avg `0.0209` n `23`; metal avg `-0.0084` n `18`; unknown avg `0.0197` n `383`
- 1h: commodity avg `0.0498` n `12`; crypto_alt avg `0.0801` n `228`; crypto_major avg `0.1308` n `8`; equity avg `0.078` n `65`; fx avg `0.0009` n `5`; index avg `0.0446` n `23`; metal avg `-0.0339` n `18`; unknown avg `-0.0379` n `383`
- 4h: commodity avg `1.7694` n `12`; crypto_alt avg `-8.875` n `228`; crypto_major avg `-2.5446` n `8`; equity avg `-2.8125` n `65`; fx avg `-0.1708` n `5`; index avg `-1.7549` n `23`; metal avg `-5.8343` n `18`; unknown avg `550.1472` n `367`
- 24h: commodity avg `1.7694` n `12`; crypto_alt avg `-8.875` n `228`; crypto_major avg `-2.5446` n `8`; equity avg `-2.8125` n `65`; fx avg `-0.1708` n `5`; index avg `-1.7549` n `23`; metal avg `-5.8343` n `18`; unknown avg `550.1472` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
