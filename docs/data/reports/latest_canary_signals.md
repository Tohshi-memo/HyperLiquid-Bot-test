# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T16:01:43.581617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5964` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0277` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9189` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.1252` n `230`; crypto_major avg `-0.1364` n `8`; equity avg `-0.1035` n `92`; fx avg `-0.0029` n `6`; index avg `-0.0365` n `25`; metal avg `-0.0385` n `20`; unknown avg `0.085` n `766`
- 1h: commodity avg `0.3467` n `12`; crypto_alt avg `-0.02` n `230`; crypto_major avg `0.1107` n `8`; equity avg `-0.1593` n `92`; fx avg `-0.0107` n `6`; index avg `-0.0639` n `25`; metal avg `-0.3376` n `20`; unknown avg `-0.2074` n `766`
- 4h: commodity avg `-0.0859` n `12`; crypto_alt avg `1.7098` n `230`; crypto_major avg `2.5105` n `8`; equity avg `0.5916` n `92`; fx avg `-0.024` n `6`; index avg `0.2` n `25`; metal avg `0.4828` n `20`; unknown avg `0.7331` n `758`
- 24h: commodity avg `0.9155` n `12`; crypto_alt avg `1.03` n `230`; crypto_major avg `2.6395` n `8`; equity avg `0.1984` n `92`; fx avg `-0.0005` n `6`; index avg `0.1858` n `25`; metal avg `0.464` n `20`; unknown avg `-0.2391` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
