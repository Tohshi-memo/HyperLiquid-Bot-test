# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T15:37:33.074832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7825` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1614` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0107` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.151` n `12`; crypto_alt avg `0.3069` n `230`; crypto_major avg `0.324` n `8`; equity avg `-0.0366` n `92`; fx avg `0.0018` n `6`; index avg `-0.0132` n `25`; metal avg `-0.1318` n `20`; unknown avg `-0.1036` n `766`
- 1h: commodity avg `0.0453` n `12`; crypto_alt avg `0.5035` n `230`; crypto_major avg `0.7478` n `8`; equity avg `0.3684` n `92`; fx avg `-0.0118` n `6`; index avg `0.0819` n `25`; metal avg `-0.0271` n `20`; unknown avg `-0.197` n `758`
- 4h: commodity avg `-0.078` n `12`; crypto_alt avg `1.9808` n `230`; crypto_major avg `2.7045` n `8`; equity avg `0.6938` n `92`; fx avg `-0.0183` n `6`; index avg `0.2679` n `25`; metal avg `0.5431` n `20`; unknown avg `0.7945` n `758`
- 24h: commodity avg `0.9602` n `12`; crypto_alt avg `1.2516` n `230`; crypto_major avg `2.7876` n `8`; equity avg `0.0796` n `92`; fx avg `0.0017` n `6`; index avg `0.171` n `25`; metal avg `0.5307` n `20`; unknown avg `-0.1952` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
