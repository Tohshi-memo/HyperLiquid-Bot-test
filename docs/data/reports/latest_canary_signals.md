# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T15:52:33.490678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.7564` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.7136` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9012` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.0308` n `228`; crypto_major avg `0.0491` n `8`; equity avg `-0.2078` n `88`; fx avg `0.0083` n `6`; index avg `-0.0539` n `25`; metal avg `0.0468` n `20`; unknown avg `0.6426` n `763`
- 1h: commodity avg `0.0292` n `12`; crypto_alt avg `0.4742` n `228`; crypto_major avg `0.7588` n `8`; equity avg `0.4304` n `88`; fx avg `-0.0303` n `6`; index avg `0.0119` n `25`; metal avg `-0.0523` n `20`; unknown avg `-0.0429` n `763`
- 4h: commodity avg `-0.2395` n `12`; crypto_alt avg `1.7949` n `228`; crypto_major avg `2.4741` n `8`; equity avg `-0.2823` n `88`; fx avg `-0.079` n `6`; index avg `-0.1937` n `25`; metal avg `0.5729` n `20`; unknown avg `1.0194` n `763`
- 24h: commodity avg `-0.6468` n `12`; crypto_alt avg `2.218` n `228`; crypto_major avg `2.1996` n `8`; equity avg `0.0832` n `88`; fx avg `-0.0292` n `6`; index avg `-0.3458` n `25`; metal avg `0.3588` n `20`; unknown avg `0.4288` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
