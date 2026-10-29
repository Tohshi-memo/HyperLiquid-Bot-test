# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T16:07:51.094763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.1188` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.734` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5606` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0287` n `13`; crypto_alt avg `0.4319` n `238`; crypto_major avg `0.3839` n `8`; equity avg `0.0811` n `156`; fx avg `0.0021` n `6`; index avg `0.0075` n `27`; metal avg `0.0099` n `20`; unknown avg `-0.1812` n `1226`
- 1h: commodity avg `0.2412` n `13`; crypto_alt avg `1.4208` n `238`; crypto_major avg `1.1944` n `8`; equity avg `0.3964` n `156`; fx avg `0.0396` n `6`; index avg `0.0247` n `27`; metal avg `0.0143` n `20`; unknown avg `18.9515` n `1226`
- 4h: commodity avg `-0.3388` n `13`; crypto_alt avg `3.0031` n `238`; crypto_major avg `2.78` n `8`; equity avg `1.2194` n `156`; fx avg `0.1079` n `6`; index avg `0.0525` n `27`; metal avg `0.046` n `20`; unknown avg `24.4896` n `1132`
- 24h: commodity avg `-0.8957` n `13`; crypto_alt avg `1.961` n `238`; crypto_major avg `3.4092` n `8`; equity avg `-0.1877` n `155`; fx avg `0.0315` n `6`; index avg `-0.0958` n `27`; metal avg `-0.4272` n `20`; unknown avg `40.6338` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
