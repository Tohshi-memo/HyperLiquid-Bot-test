# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T16:37:31.645567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9589` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.5255` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.2965` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0576` n `12`; crypto_alt avg `0.2162` n `230`; crypto_major avg `0.4679` n `8`; equity avg `0.0098` n `121`; fx avg `-0.009` n `6`; index avg `0.0147` n `25`; metal avg `-0.0064` n `20`; unknown avg `-0.061` n `792`
- 1h: commodity avg `-0.0512` n `12`; crypto_alt avg `0.2172` n `230`; crypto_major avg `1.0843` n `8`; equity avg `-0.0276` n `121`; fx avg `0.0185` n `6`; index avg `0.0219` n `25`; metal avg `-0.0665` n `20`; unknown avg `-0.0003` n `792`
- 4h: commodity avg `-0.225` n `12`; crypto_alt avg `1.3791` n `230`; crypto_major avg `2.7339` n `8`; equity avg `0.2084` n `121`; fx avg `0.0089` n `6`; index avg `0.1513` n `25`; metal avg `0.4374` n `20`; unknown avg `0.3024` n `792`
- 24h: commodity avg `-0.073` n `12`; crypto_alt avg `5.844` n `230`; crypto_major avg `9.8157` n `8`; equity avg `-0.9652` n `121`; fx avg `0.1953` n `6`; index avg `-0.0359` n `25`; metal avg `0.2365` n `20`; unknown avg `2.1645` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
