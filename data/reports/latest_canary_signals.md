# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T22:52:37.714206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.1945` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.955` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.8728` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.6278` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.4953` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.1344` n `230`; crypto_major avg `-0.5656` n `8`; equity avg `0.0821` n `121`; fx avg `0.0243` n `6`; index avg `0.0216` n `25`; metal avg `0.0121` n `20`; unknown avg `-0.0733` n `792`
- 1h: commodity avg `-0.078` n `12`; crypto_alt avg `-0.9515` n `230`; crypto_major avg `-1.4446` n `8`; equity avg `0.1832` n `121`; fx avg `0.0159` n `6`; index avg `0.0507` n `25`; metal avg `-0.0442` n `20`; unknown avg `-0.0412` n `792`
- 4h: commodity avg `-0.0572` n `12`; crypto_alt avg `1.9282` n `230`; crypto_major avg `4.1373` n `8`; equity avg `1.2645` n `121`; fx avg `-0.0033` n `6`; index avg `0.121` n `25`; metal avg `0.1823` n `20`; unknown avg `1.11` n `792`
- 24h: commodity avg `-0.1285` n `12`; crypto_alt avg `5.2449` n `230`; crypto_major avg `9.5872` n `8`; equity avg `1.1073` n `120`; fx avg `-0.1955` n `6`; index avg `0.1819` n `25`; metal avg `1.2566` n `20`; unknown avg `1.4033` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
