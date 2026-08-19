# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T23:22:24.139715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4733` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4176` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0288` n `12`; crypto_alt avg `-0.0637` n `230`; crypto_major avg `-0.2292` n `8`; equity avg `-0.0431` n `121`; fx avg `0.0001` n `6`; index avg `-0.01` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0731` n `792`
- 1h: commodity avg `0.0489` n `12`; crypto_alt avg `-0.3677` n `230`; crypto_major avg `-0.9397` n `8`; equity avg `0.1406` n `121`; fx avg `0.0271` n `6`; index avg `0.0234` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.1368` n `792`
- 4h: commodity avg `0.0686` n `12`; crypto_alt avg `1.5504` n `230`; crypto_major avg `2.5419` n `8`; equity avg `1.081` n `121`; fx avg `-0.0012` n `6`; index avg `0.1102` n `25`; metal avg `0.1243` n `20`; unknown avg `0.6109` n `792`
- 24h: commodity avg `-0.0797` n `12`; crypto_alt avg `5.0742` n `230`; crypto_major avg `9.4342` n `8`; equity avg `1.1441` n `120`; fx avg `-0.1938` n `6`; index avg `0.139` n `25`; metal avg `1.291` n `20`; unknown avg `1.4231` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
