# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T03:22:23.059733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.8536` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.4186` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.9866` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `0.0466` n `231`; crypto_major avg `-0.0484` n `8`; equity avg `0.0648` n `122`; fx avg `0.003` n `6`; index avg `0.0319` n `25`; metal avg `-0.0172` n `20`; unknown avg `-0.0022` n `794`
- 1h: commodity avg `-0.0994` n `12`; crypto_alt avg `0.2502` n `231`; crypto_major avg `0.3194` n `8`; equity avg `0.0795` n `122`; fx avg `0.0073` n `6`; index avg `0.052` n `25`; metal avg `-0.1945` n `20`; unknown avg `0.9724` n `794`
- 4h: commodity avg `0.0367` n `12`; crypto_alt avg `1.9425` n `231`; crypto_major avg `2.4553` n `8`; equity avg `0.4687` n `122`; fx avg `0.0308` n `6`; index avg `0.0587` n `25`; metal avg `-0.3983` n `20`; unknown avg `0.9999` n `794`
- 24h: commodity avg `0.0131` n `12`; crypto_alt avg `2.3212` n `231`; crypto_major avg `3.1369` n `8`; equity avg `-0.8531` n `122`; fx avg `0.0341` n `6`; index avg `-0.1281` n `25`; metal avg `-0.1918` n `20`; unknown avg `0.6177` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
