# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T20:37:30.319475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0472` n `12`; crypto_alt avg `-0.1016` n `229`; crypto_major avg `-0.1148` n `8`; equity avg `0.0227` n `91`; fx avg `-0.0043` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0808` n `20`; unknown avg `-0.0157` n `763`
- 1h: commodity avg `0.0498` n `12`; crypto_alt avg `-0.1019` n `229`; crypto_major avg `-0.1704` n `8`; equity avg `0.2451` n `91`; fx avg `0.01` n `6`; index avg `0.0463` n `25`; metal avg `-0.0671` n `20`; unknown avg `0.0179` n `763`
- 4h: commodity avg `0.4272` n `12`; crypto_alt avg `-1.3453` n `229`; crypto_major avg `-0.9126` n `8`; equity avg `-0.4745` n `91`; fx avg `0.0013` n `6`; index avg `-0.0689` n `25`; metal avg `-0.4421` n `20`; unknown avg `0.0533` n `761`
- 24h: commodity avg `0.926` n `12`; crypto_alt avg `-1.9886` n `229`; crypto_major avg `-1.2045` n `8`; equity avg `-3.2239` n `91`; fx avg `-0.2492` n `6`; index avg `-0.5973` n `25`; metal avg `-0.6105` n `20`; unknown avg `-0.2607` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
