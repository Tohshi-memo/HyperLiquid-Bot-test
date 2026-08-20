# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T18:07:28.751255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5493` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.2768` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8243` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0596` n `12`; crypto_alt avg `-0.6192` n `230`; crypto_major avg `-1.0153` n `8`; equity avg `-0.2784` n `121`; fx avg `-0.0033` n `6`; index avg `-0.051` n `25`; metal avg `-0.0304` n `20`; unknown avg `0.4826` n `792`
- 1h: commodity avg `0.0223` n `12`; crypto_alt avg `-0.4971` n `230`; crypto_major avg `-0.8383` n `8`; equity avg `-0.2441` n `121`; fx avg `0.0043` n `6`; index avg `-0.075` n `25`; metal avg `-0.0234` n `20`; unknown avg `0.5907` n `792`
- 4h: commodity avg `-0.1718` n `12`; crypto_alt avg `1.0167` n `230`; crypto_major avg `2.105` n `8`; equity avg `-0.4443` n `121`; fx avg `0.0081` n `6`; index avg `-0.082` n `25`; metal avg `0.2807` n `20`; unknown avg `1.3075` n `792`
- 24h: commodity avg `0.0428` n `12`; crypto_alt avg `6.3556` n `230`; crypto_major avg `10.4835` n `8`; equity avg `-0.4189` n `121`; fx avg `0.1979` n `6`; index avg `-0.036` n `25`; metal avg `0.2953` n `20`; unknown avg `3.8207` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
