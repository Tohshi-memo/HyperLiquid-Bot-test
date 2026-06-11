# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T18:22:31.450991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `3.1169` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `2.7651` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.2364` n `12`; crypto_alt avg `-0.1866` n `228`; crypto_major avg `0.0502` n `8`; equity avg `0.1383` n `74`; fx avg `0.0144` n `6`; index avg `0.0362` n `23`; metal avg `0.3689` n `18`; unknown avg `-0.0483` n `556`
- 1h: commodity avg `-1.0704` n `12`; crypto_alt avg `1.7177` n `228`; crypto_major avg `2.0465` n `8`; equity avg `1.7101` n `74`; fx avg `0.0699` n `6`; index avg `0.9005` n `23`; metal avg `1.9197` n `18`; unknown avg `1.5287` n `556`
- 4h: commodity avg `-1.1752` n `12`; crypto_alt avg `1.1545` n `228`; crypto_major avg `1.5899` n `8`; equity avg `1.3692` n `74`; fx avg `-0.0004` n `6`; index avg `0.7726` n `23`; metal avg `1.8146` n `18`; unknown avg `0.3687` n `556`
- 24h: commodity avg `-1.7448` n `12`; crypto_alt avg `2.7988` n `228`; crypto_major avg `2.9707` n `8`; equity avg `1.3634` n `74`; fx avg `-0.002` n `6`; index avg `1.0269` n `23`; metal avg `1.2666` n `18`; unknown avg `2.5701` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
