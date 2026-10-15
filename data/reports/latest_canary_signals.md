# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T17:38:29.863817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.0537` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.7554` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.1375` n `13`; crypto_alt avg `-0.3525` n `236`; crypto_major avg `-0.2526` n `8`; equity avg `0.2604` n `151`; fx avg `0.0236` n `6`; index avg `0.0312` n `26`; metal avg `0.0158` n `20`; unknown avg `0.4323` n `1136`
- 1h: commodity avg `0.0548` n `13`; crypto_alt avg `0.4768` n `236`; crypto_major avg `0.5352` n `8`; equity avg `0.5062` n `151`; fx avg `0.0224` n `6`; index avg `0.0692` n `26`; metal avg `0.0331` n `20`; unknown avg `0.6597` n `1134`
- 4h: commodity avg `0.268` n `13`; crypto_alt avg `4.3629` n `236`; crypto_major avg `3.0234` n `8`; equity avg `2.6391` n `151`; fx avg `0.0439` n `6`; index avg `0.339` n `26`; metal avg `-0.0303` n `20`; unknown avg `4.4656` n `1082`
- 24h: commodity avg `-0.0203` n `13`; crypto_alt avg `0.6669` n `236`; crypto_major avg `0.5371` n `8`; equity avg `-1.1442` n `151`; fx avg `0.1956` n `6`; index avg `-0.1844` n `26`; metal avg `0.3876` n `20`; unknown avg `0.626` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.085`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0839`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0838`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.079`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0563`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
