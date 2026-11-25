# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T21:07:27.356295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.566` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8067` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0354` n `13`; crypto_alt avg `0.2811` n `239`; crypto_major avg `0.291` n `8`; equity avg `0.3906` n `168`; fx avg `-0.0077` n `6`; index avg `0.0392` n `27`; metal avg `0.0082` n `20`; unknown avg `41.2681` n `1227`
- 1h: commodity avg `0.1169` n `13`; crypto_alt avg `0.3998` n `239`; crypto_major avg `0.4892` n `8`; equity avg `0.3087` n `168`; fx avg `-0.0149` n `6`; index avg `0.0314` n `27`; metal avg `0.0937` n `20`; unknown avg `0.4266` n `1219`
- 4h: commodity avg `0.0905` n `13`; crypto_alt avg `2.5542` n `239`; crypto_major avg `2.6565` n `8`; equity avg `3.8785` n `168`; fx avg `0.0159` n `6`; index avg `0.3808` n `27`; metal avg `0.8498` n `20`; unknown avg `6.8451` n `1210`
- 24h: commodity avg `0.4272` n `13`; crypto_alt avg `2.4396` n `239`; crypto_major avg `1.5907` n `8`; equity avg `-0.3289` n `168`; fx avg `0.0401` n `6`; index avg `-0.05` n `27`; metal avg `0.2086` n `20`; unknown avg `29.373` n `1069`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
