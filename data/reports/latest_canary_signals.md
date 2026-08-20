# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T00:37:22.318981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.4695` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.4258` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.8026` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `0.1275` n `230`; crypto_major avg `0.1781` n `8`; equity avg `0.063` n `121`; fx avg `0.0388` n `6`; index avg `0.0232` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.0185` n `792`
- 1h: commodity avg `0.0675` n `12`; crypto_alt avg `0.5547` n `230`; crypto_major avg `0.2041` n `8`; equity avg `0.0482` n `121`; fx avg `-0.0018` n `6`; index avg `0.0177` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.0384` n `792`
- 4h: commodity avg `0.0569` n `12`; crypto_alt avg `1.8198` n `230`; crypto_major avg `2.4827` n `8`; equity avg `0.6801` n `121`; fx avg `0.0056` n `6`; index avg `0.1395` n `25`; metal avg `0.0132` n `20`; unknown avg `0.4281` n `792`
- 24h: commodity avg `-0.1079` n `12`; crypto_alt avg `5.9868` n `230`; crypto_major avg `10.1089` n `8`; equity avg `1.3236` n `120`; fx avg `-0.1445` n `6`; index avg `0.2332` n `25`; metal avg `1.1845` n `20`; unknown avg `1.4943` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
