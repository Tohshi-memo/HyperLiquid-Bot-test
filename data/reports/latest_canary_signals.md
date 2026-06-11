# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T08:37:30.535111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1463` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0532` n `12`; crypto_alt avg `0.259` n `228`; crypto_major avg `0.2709` n `8`; equity avg `0.1936` n `74`; fx avg `-0.0048` n `6`; index avg `0.0275` n `23`; metal avg `0.0608` n `18`; unknown avg `-0.0273` n `556`
- 1h: commodity avg `-0.192` n `12`; crypto_alt avg `0.7207` n `228`; crypto_major avg `0.6653` n `8`; equity avg `0.5141` n `74`; fx avg `-0.0265` n `6`; index avg `0.227` n `23`; metal avg `0.0037` n `18`; unknown avg `0.1576` n `556`
- 4h: commodity avg `-1.1657` n `12`; crypto_alt avg `0.8099` n `228`; crypto_major avg `0.9806` n `8`; equity avg `0.9955` n `74`; fx avg `0.0258` n `6`; index avg `0.3698` n `23`; metal avg `0.5828` n `18`; unknown avg `0.1436` n `530`
- 24h: commodity avg `0.2856` n `12`; crypto_alt avg `1.8775` n `228`; crypto_major avg `1.9504` n `8`; equity avg `0.9143` n `74`; fx avg `0.0199` n `6`; index avg `0.0011` n `23`; metal avg `-0.0187` n `18`; unknown avg `3.7216` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
