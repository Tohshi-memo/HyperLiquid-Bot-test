# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T21:52:33.115853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `6.1403` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `5.5986` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `5.0323` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.9846` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.7723` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `0.2639` n `230`; crypto_major avg `0.2672` n `8`; equity avg `0.0622` n `121`; fx avg `0.0135` n `6`; index avg `0.0099` n `25`; metal avg `0.0177` n `20`; unknown avg `0.0374` n `792`
- 1h: commodity avg `0.0493` n `12`; crypto_alt avg `0.9971` n `230`; crypto_major avg `2.0394` n `8`; equity avg `0.2671` n `121`; fx avg `-0.0078` n `6`; index avg `0.0439` n `25`; metal avg `0.0548` n `20`; unknown avg `0.3009` n `792`
- 4h: commodity avg `-0.2335` n `12`; crypto_alt avg `2.9762` n `230`; crypto_major avg `5.9068` n `8`; equity avg `0.8745` n `121`; fx avg `-0.0238` n `6`; index avg `0.0712` n `25`; metal avg `0.3082` n `20`; unknown avg `1.6752` n `792`
- 24h: commodity avg `-0.0168` n `12`; crypto_alt avg `6.2669` n `230`; crypto_major avg `11.1916` n `8`; equity avg `0.7224` n `120`; fx avg `-0.2119` n `6`; index avg `0.1019` n `25`; metal avg `1.2485` n `20`; unknown avg `1.4259` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
