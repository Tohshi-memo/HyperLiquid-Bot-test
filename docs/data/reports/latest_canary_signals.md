# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T20:22:29.234970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.064` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9013` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0084` n `12`; crypto_alt avg `0.6638` n `233`; crypto_major avg `0.9356` n `8`; equity avg `0.1875` n `136`; fx avg `-0.0078` n `6`; index avg `0.0143` n `27`; metal avg `0.0541` n `20`; unknown avg `0.1342` n `908`
- 1h: commodity avg `0.0718` n `12`; crypto_alt avg `0.568` n `233`; crypto_major avg `0.9388` n `8`; equity avg `-0.1843` n `136`; fx avg `0.0128` n `6`; index avg `-0.0702` n `27`; metal avg `-0.0568` n `20`; unknown avg `9.4204` n `894`
- 4h: commodity avg `-0.1786` n `12`; crypto_alt avg `1.2674` n `233`; crypto_major avg `1.8205` n `8`; equity avg `-0.2435` n `136`; fx avg `0.0235` n `6`; index avg `-0.0746` n `27`; metal avg `-0.0808` n `20`; unknown avg `0.2003` n `866`
- 24h: commodity avg `0.1771` n `12`; crypto_alt avg `1.0926` n `233`; crypto_major avg `3.4048` n `8`; equity avg `-0.5827` n `136`; fx avg `0.0576` n `6`; index avg `-0.2142` n `27`; metal avg `-0.4106` n `20`; unknown avg `6.5808` n `684`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
