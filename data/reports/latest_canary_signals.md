# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T21:07:34.531919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `5.9528` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `5.3367` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `4.8848` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `3.3771` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.3402` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `3.0653` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0884` n `12`; crypto_alt avg `0.9659` n `230`; crypto_major avg `1.6219` n `8`; equity avg `0.2536` n `121`; fx avg `-0.0208` n `6`; index avg `0.0284` n `25`; metal avg `0.0671` n `20`; unknown avg `2.7413` n `792`
- 1h: commodity avg `0.1122` n `12`; crypto_alt avg `2.0555` n `230`; crypto_major avg `3.4893` n `8`; equity avg `0.424` n `121`; fx avg `-0.0266` n `6`; index avg `0.0615` n `25`; metal avg `0.1491` n `20`; unknown avg `3.0952` n `792`
- 4h: commodity avg `-0.309` n `12`; crypto_alt avg `2.9181` n `230`; crypto_major avg `5.6438` n `8`; equity avg `0.759` n `121`; fx avg `-0.0338` n `6`; index avg `0.0308` n `25`; metal avg `0.3071` n `20`; unknown avg `4.294` n `792`
- 24h: commodity avg `-0.0006` n `12`; crypto_alt avg `6.156` n `230`; crypto_major avg `10.6516` n `8`; equity avg `0.6076` n `120`; fx avg `-0.223` n `6`; index avg `0.0749` n `25`; metal avg `1.2664` n `20`; unknown avg `4.1278` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
