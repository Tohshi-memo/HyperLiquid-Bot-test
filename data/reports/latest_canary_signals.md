# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T18:37:31.165626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4004` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.0056` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0411` n `13`; crypto_alt avg `0.0083` n `239`; crypto_major avg `-0.0057` n `8`; equity avg `0.3867` n `168`; fx avg `0.0101` n `6`; index avg `0.0326` n `27`; metal avg `0.0695` n `20`; unknown avg `158.0246` n `1267`
- 1h: commodity avg `-0.0417` n `13`; crypto_alt avg `0.594` n `239`; crypto_major avg `0.685` n `8`; equity avg `1.75` n `168`; fx avg `0.0206` n `6`; index avg `0.1639` n `27`; metal avg `0.3344` n `20`; unknown avg `1.4512` n `1265`
- 4h: commodity avg `0.2592` n `13`; crypto_alt avg `3.6025` n `239`; crypto_major avg `3.6596` n `8`; equity avg `4.074` n `168`; fx avg `0.0864` n `6`; index avg `0.4234` n `27`; metal avg `0.654` n `20`; unknown avg `205.488` n `1251`
- 24h: commodity avg `0.2483` n `13`; crypto_alt avg `0.6463` n `239`; crypto_major avg `-0.2857` n `8`; equity avg `-1.8853` n `168`; fx avg `0.0078` n `6`; index avg `-0.1939` n `27`; metal avg `-0.2577` n `20`; unknown avg `436.539` n `1087`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
