# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T23:52:28.809498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1532` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1246` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `-0.1438` n `230`; crypto_major avg `-0.5556` n `8`; equity avg `-0.0279` n `121`; fx avg `-0.0012` n `6`; index avg `-0.02` n `25`; metal avg `-0.0034` n `20`; unknown avg `0.1588` n `792`
- 1h: commodity avg `0.043` n `12`; crypto_alt avg `0.0598` n `230`; crypto_major avg `-0.2143` n `8`; equity avg `0.0306` n `121`; fx avg `0.0019` n `6`; index avg `-0.0211` n `25`; metal avg `-0.0123` n `20`; unknown avg `-0.0015` n `792`
- 4h: commodity avg `0.0343` n `12`; crypto_alt avg `1.2957` n `230`; crypto_major avg `2.1875` n `8`; equity avg `0.8592` n `121`; fx avg `0.0022` n `6`; index avg `0.1172` n `25`; metal avg `0.0629` n `20`; unknown avg `0.5326` n `792`
- 24h: commodity avg `-0.0991` n `12`; crypto_alt avg `5.0666` n `230`; crypto_major avg `9.0866` n `8`; equity avg `1.3155` n `120`; fx avg `-0.2061` n `6`; index avg `0.1514` n `25`; metal avg `1.276` n `20`; unknown avg `1.3949` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
