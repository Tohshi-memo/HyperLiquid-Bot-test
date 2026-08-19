# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T20:41:23.978069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4333` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.1265` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9168` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.0863` n `230`; crypto_major avg `0.3766` n `8`; equity avg `0.0688` n `121`; fx avg `0.0013` n `6`; index avg `0.0069` n `25`; metal avg `0.0576` n `20`; unknown avg `0.322` n `792`
- 1h: commodity avg `0.0719` n `12`; crypto_alt avg `0.3892` n `230`; crypto_major avg `0.6604` n `8`; equity avg `0.324` n `121`; fx avg `0.0012` n `6`; index avg `0.0018` n `25`; metal avg `0.0766` n `20`; unknown avg `0.5225` n `792`
- 4h: commodity avg `-0.342` n `12`; crypto_alt avg `0.7271` n `230`; crypto_major avg `2.0913` n `8`; equity avg `-0.0352` n `121`; fx avg `-0.0107` n `6`; index avg `-0.0528` n `25`; metal avg `0.1745` n `20`; unknown avg `0.8848` n `792`
- 24h: commodity avg `-0.0793` n `12`; crypto_alt avg `3.9578` n `230`; crypto_major avg `7.255` n `8`; equity avg `0.0919` n `120`; fx avg `-0.2025` n `6`; index avg `0.0068` n `25`; metal avg `1.1686` n `20`; unknown avg `1.0341` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
