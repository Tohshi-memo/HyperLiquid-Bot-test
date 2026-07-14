# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T14:52:26.675415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.591` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.0619` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0969` n `12`; crypto_alt avg `-0.0192` n `230`; crypto_major avg `0.1644` n `8`; equity avg `-0.0485` n `92`; fx avg `0.0095` n `6`; index avg `0.0073` n `25`; metal avg `0.0752` n `20`; unknown avg `-0.0253` n `766`
- 1h: commodity avg `-0.2284` n `12`; crypto_alt avg `0.0679` n `230`; crypto_major avg `0.2368` n `8`; equity avg `-0.1701` n `92`; fx avg `0.0074` n `6`; index avg `-0.0088` n `25`; metal avg `0.1092` n `20`; unknown avg `19.1712` n `766`
- 4h: commodity avg `-0.4675` n `12`; crypto_alt avg `1.4825` n `230`; crypto_major avg `2.1235` n `8`; equity avg `0.0616` n `92`; fx avg `0.0046` n `6`; index avg `0.229` n `25`; metal avg `0.6798` n `20`; unknown avg `0.9441` n `766`
- 24h: commodity avg `0.9184` n `12`; crypto_alt avg `0.6186` n `230`; crypto_major avg `2.1411` n `8`; equity avg `-0.1751` n `92`; fx avg `0.0081` n `6`; index avg `0.115` n `25`; metal avg `0.7092` n `20`; unknown avg `-0.1557` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
