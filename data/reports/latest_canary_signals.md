# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T15:52:31.774644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4825` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0374` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9643` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0753` n `12`; crypto_alt avg `-0.2277` n `230`; crypto_major avg `-0.1855` n `8`; equity avg `-0.1951` n `92`; fx avg `0.0074` n `6`; index avg `-0.0429` n `25`; metal avg `-0.087` n `20`; unknown avg `-0.048` n `766`
- 1h: commodity avg `0.2183` n `12`; crypto_alt avg `0.2948` n `230`; crypto_major avg `0.3957` n `8`; equity avg `0.2197` n `92`; fx avg `-0.0139` n `6`; index avg `0.0313` n `25`; metal avg `-0.1887` n `20`; unknown avg `-0.2609` n `758`
- 4h: commodity avg `0.0028` n `12`; crypto_alt avg `1.7478` n `230`; crypto_major avg `2.4853` n `8`; equity avg `0.521` n `92`; fx avg `-0.0261` n `6`; index avg `0.2007` n `25`; metal avg `0.4479` n `20`; unknown avg `0.7948` n `758`
- 24h: commodity avg `0.9658` n `12`; crypto_alt avg `1.223` n `230`; crypto_major avg `2.7024` n `8`; equity avg `0.2276` n `92`; fx avg `0.0007` n `6`; index avg `0.2012` n `25`; metal avg `0.5038` n `20`; unknown avg `-0.2074` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
