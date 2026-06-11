# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T20:22:37.559962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.6586` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0304` n `12`; crypto_alt avg `0.0212` n `228`; crypto_major avg `-0.1865` n `8`; equity avg `-0.1169` n `74`; fx avg `-0.0013` n `6`; index avg `-0.0213` n `23`; metal avg `-0.0135` n `18`; unknown avg `0.175` n `556`
- 1h: commodity avg `-0.5877` n `12`; crypto_alt avg `0.1549` n `228`; crypto_major avg `-0.2336` n `8`; equity avg `0.3785` n `74`; fx avg `-0.0237` n `6`; index avg `0.4303` n `23`; metal avg `0.2836` n `18`; unknown avg `0.1387` n `556`
- 4h: commodity avg `-1.8255` n `12`; crypto_alt avg `1.4532` n `228`; crypto_major avg `1.8331` n `8`; equity avg `2.1444` n `74`; fx avg `0.0617` n `6`; index avg `1.3136` n `23`; metal avg `2.536` n `18`; unknown avg `0.2517` n `556`
- 24h: commodity avg `-2.163` n `12`; crypto_alt avg `3.7171` n `228`; crypto_major avg `3.5783` n `8`; equity avg `3.6385` n `74`; fx avg `0.0293` n `6`; index avg `2.3499` n `23`; metal avg `3.4729` n `18`; unknown avg `2.2748` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
