# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T07:52:23.606877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.3603` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1882` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.1015` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0553` n `12`; crypto_alt avg `0.0077` n `228`; crypto_major avg `0.1203` n `8`; equity avg `0.1536` n `72`; fx avg `-0.0215` n `6`; index avg `0.0272` n `23`; metal avg `-0.0147` n `18`; unknown avg `0.3956` n `420`
- 1h: commodity avg `0.2179` n `12`; crypto_alt avg `0.2869` n `228`; crypto_major avg `0.3892` n `8`; equity avg `0.0351` n `72`; fx avg `-0.0094` n `6`; index avg `0.0377` n `23`; metal avg `-0.0793` n `18`; unknown avg `0.3308` n `420`
- 4h: commodity avg `0.5383` n `12`; crypto_alt avg `3.6799` n `228`; crypto_major avg `2.6398` n `8`; equity avg `0.4516` n `72`; fx avg `0.0496` n `6`; index avg `-0.0143` n `23`; metal avg `-0.7205` n `18`; unknown avg `0.883` n `410`
- 24h: commodity avg `1.4251` n `12`; crypto_alt avg `-1.0829` n `228`; crypto_major avg `-3.3037` n `8`; equity avg `0.9117` n `72`; fx avg `0.023` n `6`; index avg `1.0063` n `23`; metal avg `-1.8067` n `18`; unknown avg `0.4772` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.042`, n `668`, weak_sample_signal
