# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T17:37:35.100809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5354` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5238` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7772` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0687` n `12`; crypto_alt avg `-0.0822` n `229`; crypto_major avg `-0.2222` n `8`; equity avg `-0.2232` n `88`; fx avg `-0.0018` n `6`; index avg `-0.0417` n `25`; metal avg `0.0809` n `20`; unknown avg `0.0602` n `766`
- 1h: commodity avg `0.0278` n `12`; crypto_alt avg `-0.1425` n `229`; crypto_major avg `-0.1109` n `8`; equity avg `-0.4479` n `88`; fx avg `0.0135` n `6`; index avg `-0.0781` n `25`; metal avg `0.1755` n `20`; unknown avg `0.0433` n `766`
- 4h: commodity avg `0.0969` n `12`; crypto_alt avg `2.6734` n `229`; crypto_major avg `2.6323` n `8`; equity avg `0.8551` n `88`; fx avg `0.0269` n `6`; index avg `0.0712` n `25`; metal avg `0.1085` n `20`; unknown avg `3.6404` n `765`
- 24h: commodity avg `-0.0816` n `12`; crypto_alt avg `1.0718` n `229`; crypto_major avg `0.7015` n `8`; equity avg `-0.4284` n `88`; fx avg `0.2032` n `6`; index avg `0.007` n `25`; metal avg `-0.2336` n `20`; unknown avg `0.8247` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
