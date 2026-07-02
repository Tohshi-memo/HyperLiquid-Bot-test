# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T13:07:30.113588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4678` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9033` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0344` n `12`; crypto_alt avg `0.0261` n `229`; crypto_major avg `0.02` n `8`; equity avg `-0.299` n `88`; fx avg `0.0124` n `6`; index avg `-0.0769` n `25`; metal avg `-0.0995` n `20`; unknown avg `-0.2136` n `763`
- 1h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.2419` n `229`; crypto_major avg `0.323` n `8`; equity avg `0.3826` n `88`; fx avg `0.0507` n `6`; index avg `0.0828` n `25`; metal avg `0.4858` n `20`; unknown avg `0.0355` n `763`
- 4h: commodity avg `-0.1046` n `12`; crypto_alt avg `1.3932` n `228`; crypto_major avg `2.3632` n `8`; equity avg `1.0488` n `88`; fx avg `0.0062` n `6`; index avg `0.1891` n `25`; metal avg `0.4599` n `20`; unknown avg `-0.0351` n `763`
- 24h: commodity avg `-0.5856` n `12`; crypto_alt avg `3.5842` n `228`; crypto_major avg `4.655` n `8`; equity avg `-0.0137` n `88`; fx avg `-0.0343` n `6`; index avg `-0.2983` n `25`; metal avg `1.2914` n `20`; unknown avg `1.7749` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
