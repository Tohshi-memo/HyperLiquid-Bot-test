# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T22:07:24.360425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `5.9269` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `5.4287` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `4.5827` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0401` n `12`; crypto_alt avg `-0.4331` n `230`; crypto_major avg `-0.3747` n `8`; equity avg `0.0538` n `121`; fx avg `-0.0119` n `6`; index avg `0.0134` n `25`; metal avg `-0.0094` n `20`; unknown avg `0.004` n `792`
- 1h: commodity avg `-0.0583` n `12`; crypto_alt avg `-0.3491` n `230`; crypto_major avg `0.4956` n `8`; equity avg `0.1561` n `121`; fx avg `0.0038` n `6`; index avg `0.0243` n `25`; metal avg `-0.009` n `20`; unknown avg `0.0571` n `792`
- 4h: commodity avg `-0.2054` n `12`; crypto_alt avg `2.678` n `230`; crypto_major avg `5.7215` n `8`; equity avg `1.1388` n `121`; fx avg `-0.0251` n `6`; index avg `0.1057` n `25`; metal avg `0.2928` n `20`; unknown avg `1.7143` n `792`
- 24h: commodity avg `-0.0981` n `12`; crypto_alt avg `5.7111` n `230`; crypto_major avg `10.7147` n `8`; equity avg `0.7454` n `120`; fx avg `-0.2251` n `6`; index avg `0.1001` n `25`; metal avg `1.2532` n `20`; unknown avg `1.3952` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
