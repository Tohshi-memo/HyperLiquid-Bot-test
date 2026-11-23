# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T15:07:37.181982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.5735` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.6245` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.2431` n `13`; crypto_alt avg `0.2369` n `239`; crypto_major avg `0.5309` n `8`; equity avg `1.5122` n `166`; fx avg `-0.0209` n `6`; index avg `0.1369` n `27`; metal avg `0.0254` n `20`; unknown avg `0.4404` n `1258`
- 1h: commodity avg `-0.3475` n `13`; crypto_alt avg `1.0618` n `239`; crypto_major avg `0.7513` n `8`; equity avg `0.2006` n `166`; fx avg `-0.0411` n `6`; index avg `0.0394` n `27`; metal avg `0.0569` n `20`; unknown avg `317.7889` n `1262`
- 4h: commodity avg `-0.4328` n `13`; crypto_alt avg `3.3664` n `239`; crypto_major avg `4.1407` n `8`; equity avg `4.5208` n `166`; fx avg `-0.1633` n `6`; index avg `0.5228` n `27`; metal avg `0.5162` n `20`; unknown avg `9.9371` n `1252`
- 24h: commodity avg `-1.3223` n `13`; crypto_alt avg `4.1401` n `239`; crypto_major avg `5.3093` n `8`; equity avg `6.7539` n `166`; fx avg `0.018` n `6`; index avg `0.6125` n `27`; metal avg `0.9315` n `20`; unknown avg `9.731` n `1061`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
