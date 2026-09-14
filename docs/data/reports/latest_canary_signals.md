# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T18:52:29.398426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4616` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7455` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `0.0425` n `233`; crypto_major avg `0.1331` n `8`; equity avg `-0.002` n `136`; fx avg `-0.0112` n `6`; index avg `-0.0082` n `27`; metal avg `-0.0258` n `20`; unknown avg `-0.1152` n `908`
- 1h: commodity avg `-0.1891` n `12`; crypto_alt avg `0.3685` n `233`; crypto_major avg `0.7434` n `8`; equity avg `-0.1621` n `136`; fx avg `-0.0194` n `6`; index avg `-0.0156` n `27`; metal avg `-0.007` n `20`; unknown avg `0.1522` n `906`
- 4h: commodity avg `-0.4931` n `12`; crypto_alt avg `1.6023` n `233`; crypto_major avg `1.9685` n `8`; equity avg `1.0859` n `136`; fx avg `-0.008` n `6`; index avg `0.2203` n `27`; metal avg `0.223` n `20`; unknown avg `0.2184` n `878`
- 24h: commodity avg `0.0756` n `12`; crypto_alt avg `0.4081` n `233`; crypto_major avg `2.6099` n `8`; equity avg `-0.2751` n `136`; fx avg `0.045` n `6`; index avg `-0.1164` n `27`; metal avg `-0.3237` n `20`; unknown avg `3.148` n `696`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
