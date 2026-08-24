# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T12:52:30.199786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.3001` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.0938` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `0.5294` n `231`; crypto_major avg `0.404` n `8`; equity avg `0.1253` n `122`; fx avg `0.0019` n `6`; index avg `0.0126` n `25`; metal avg `0.0439` n `20`; unknown avg `-0.0491` n `793`
- 1h: commodity avg `0.0376` n `12`; crypto_alt avg `0.7092` n `231`; crypto_major avg `0.8541` n `8`; equity avg `-0.0413` n `122`; fx avg `-0.0235` n `6`; index avg `-0.0328` n `25`; metal avg `0.1151` n `20`; unknown avg `0.0902` n `793`
- 4h: commodity avg `0.2805` n `12`; crypto_alt avg `1.9477` n `231`; crypto_major avg `2.2632` n `8`; equity avg `-0.0369` n `122`; fx avg `-0.0253` n `6`; index avg `-0.0223` n `25`; metal avg `0.1694` n `20`; unknown avg `0.9226` n `793`
- 24h: commodity avg `0.003` n `12`; crypto_alt avg `1.8056` n `231`; crypto_major avg `1.4332` n `8`; equity avg `-1.479` n `122`; fx avg `-0.1426` n `6`; index avg `-0.1594` n `25`; metal avg `0.2442` n `20`; unknown avg `3.8012` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
