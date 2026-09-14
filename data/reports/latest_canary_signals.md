# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T20:37:39.560510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1608` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1164` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1145` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `0.0466` n `233`; crypto_major avg `-0.084` n `8`; equity avg `0.0555` n `136`; fx avg `0.0024` n `6`; index avg `0.0115` n `27`; metal avg `0.0014` n `20`; unknown avg `0.6825` n `888`
- 1h: commodity avg `0.0587` n `12`; crypto_alt avg `0.8714` n `233`; crypto_major avg `1.1435` n `8`; equity avg `-0.0512` n `136`; fx avg `0.0064` n `6`; index avg `-0.0313` n `27`; metal avg `-0.0237` n `20`; unknown avg `3.3565` n `874`
- 4h: commodity avg `-0.152` n `12`; crypto_alt avg `1.4937` n `233`; crypto_major avg `2.0088` n `8`; equity avg `-0.1057` n `136`; fx avg `0.0212` n `6`; index avg `-0.0566` n `27`; metal avg `-0.1076` n `20`; unknown avg `0.854` n `852`
- 24h: commodity avg `0.1783` n `12`; crypto_alt avg `1.0888` n `233`; crypto_major avg `3.249` n `8`; equity avg `-0.561` n `136`; fx avg `0.0588` n `6`; index avg `-0.2136` n `27`; metal avg `-0.3996` n `20`; unknown avg `6.7565` n `684`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
