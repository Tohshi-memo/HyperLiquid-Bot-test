# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T14:22:30.940871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6419` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4748` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6645` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0117` n `13`; crypto_alt avg `-0.0775` n `238`; crypto_major avg `0.0667` n `8`; equity avg `0.1335` n `156`; fx avg `0.0422` n `6`; index avg `0.0136` n `27`; metal avg `0.0625` n `20`; unknown avg `31.4163` n `1238`
- 1h: commodity avg `0.1707` n `13`; crypto_alt avg `-0.0294` n `238`; crypto_major avg `0.028` n `8`; equity avg `0.6098` n `156`; fx avg `0.0758` n `6`; index avg `-0.0107` n `27`; metal avg `-0.0136` n `20`; unknown avg `0.4911` n `1164`
- 4h: commodity avg `-0.2814` n `13`; crypto_alt avg `1.2985` n `238`; crypto_major avg `2.3605` n `8`; equity avg `0.696` n `155`; fx avg `0.0366` n `6`; index avg `-0.0542` n `27`; metal avg `-0.1143` n `20`; unknown avg `6.8152` n `1112`
- 24h: commodity avg `-0.7197` n `13`; crypto_alt avg `0.2163` n `238`; crypto_major avg `1.6732` n `8`; equity avg `-0.2132` n `155`; fx avg `0.02` n `6`; index avg `-0.0791` n `27`; metal avg `-0.448` n `20`; unknown avg `13.6256` n `976`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
