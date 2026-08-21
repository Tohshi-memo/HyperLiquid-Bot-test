# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T02:07:24.579110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0179` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9102` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `0.0887` n `230`; crypto_major avg `-0.1858` n `8`; equity avg `0.0969` n `121`; fx avg `0.014` n `6`; index avg `0.0171` n `25`; metal avg `0.0246` n `20`; unknown avg `0.1288` n `793`
- 1h: commodity avg `0.0743` n `12`; crypto_alt avg `0.6337` n `230`; crypto_major avg `1.0749` n `8`; equity avg `0.5289` n `121`; fx avg `-0.0581` n `6`; index avg `0.0977` n `25`; metal avg `0.1154` n `20`; unknown avg `0.1821` n `793`
- 4h: commodity avg `0.1017` n `12`; crypto_alt avg `1.1359` n `230`; crypto_major avg `2.1196` n `8`; equity avg `0.8171` n `121`; fx avg `-0.0953` n `6`; index avg `0.118` n `25`; metal avg `0.2094` n `20`; unknown avg `-0.2368` n `793`
- 24h: commodity avg `0.3788` n `12`; crypto_alt avg `5.1027` n `230`; crypto_major avg `6.9459` n `8`; equity avg `-0.6756` n `121`; fx avg `-0.0252` n `6`; index avg `-0.1561` n `25`; metal avg `0.4303` n `20`; unknown avg `2.649` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
