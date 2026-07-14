# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T15:07:26.955714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9057` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.6454` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5169` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1467` n `12`; crypto_alt avg `0.1933` n `230`; crypto_major avg `0.1481` n `8`; equity avg `0.2758` n `92`; fx avg `-0.006` n `6`; index avg `0.0588` n `25`; metal avg `0.1121` n `20`; unknown avg `0.001` n `758`
- 1h: commodity avg `-0.2363` n `12`; crypto_alt avg `0.4074` n `230`; crypto_major avg `0.5029` n `8`; equity avg `0.4709` n `92`; fx avg `-0.0058` n `6`; index avg `0.1062` n `25`; metal avg `0.2036` n `20`; unknown avg `-0.1286` n `758`
- 4h: commodity avg `-0.5626` n `12`; crypto_alt avg `1.746` n `230`; crypto_major avg `2.3431` n `8`; equity avg `0.6977` n `92`; fx avg `-0.0035` n `6`; index avg `0.3068` n `25`; metal avg `0.8262` n `20`; unknown avg `0.7898` n `758`
- 24h: commodity avg `0.6771` n `12`; crypto_alt avg `0.6423` n `230`; crypto_major avg `2.1243` n `8`; equity avg `-0.1517` n `92`; fx avg `0.0043` n `6`; index avg `0.1371` n `25`; metal avg `0.7798` n `20`; unknown avg `-0.2628` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
