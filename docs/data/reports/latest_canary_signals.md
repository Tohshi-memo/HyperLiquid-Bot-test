# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T16:37:28.755510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6999` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.2361` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9344` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.035` n `12`; crypto_alt avg `0.1083` n `228`; crypto_major avg `0.0771` n `8`; equity avg `0.0219` n `88`; fx avg `-0.0008` n `6`; index avg `-0.0146` n `25`; metal avg `-0.0176` n `20`; unknown avg `0.2387` n `763`
- 1h: commodity avg `0.0313` n `12`; crypto_alt avg `-0.0155` n `228`; crypto_major avg `0.0487` n `8`; equity avg `-0.0476` n `88`; fx avg `0.0085` n `6`; index avg `-0.0488` n `25`; metal avg `0.0544` n `20`; unknown avg `1.0504` n `763`
- 4h: commodity avg `-0.0725` n `12`; crypto_alt avg `1.9762` n `228`; crypto_major avg `2.6274` n `8`; equity avg `0.3913` n `88`; fx avg `-0.0527` n `6`; index avg `-0.1283` n `25`; metal avg `0.693` n `20`; unknown avg `1.3298` n `763`
- 24h: commodity avg `-0.6811` n `12`; crypto_alt avg `2.5523` n `228`; crypto_major avg `2.6034` n `8`; equity avg `-0.0566` n `88`; fx avg `-0.011` n `6`; index avg `-0.3755` n `25`; metal avg `0.3634` n `20`; unknown avg `0.6451` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
