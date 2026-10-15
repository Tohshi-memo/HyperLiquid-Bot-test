# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T17:07:39.285648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.4087` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1883` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `-0.2411` n `236`; crypto_major avg `0.001` n `8`; equity avg `0.2753` n `151`; fx avg `-0.0077` n `6`; index avg `0.0313` n `26`; metal avg `-0.0346` n `20`; unknown avg `0.2709` n `1134`
- 1h: commodity avg `-0.0624` n `13`; crypto_alt avg `-0.3645` n `236`; crypto_major avg `-0.3787` n `8`; equity avg `-0.0314` n `151`; fx avg `0.0132` n `6`; index avg `0.0016` n `26`; metal avg `-0.0428` n `20`; unknown avg `0.8868` n `1134`
- 4h: commodity avg `0.2132` n `13`; crypto_alt avg `3.8893` n `236`; crypto_major avg `2.4015` n `8`; equity avg `1.7362` n `151`; fx avg `0.0217` n `6`; index avg `0.2648` n `26`; metal avg `-0.0072` n `20`; unknown avg `2.2077` n `1082`
- 24h: commodity avg `-0.1402` n `13`; crypto_alt avg `-0.0628` n `236`; crypto_major avg `-0.1377` n `8`; equity avg `-1.8807` n `151`; fx avg `0.1945` n `6`; index avg `-0.2865` n `26`; metal avg `0.3345` n `20`; unknown avg `0.1416` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0899`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0873`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0834`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0723`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.061`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
