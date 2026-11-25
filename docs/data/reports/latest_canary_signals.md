# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T20:22:29.192312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9545` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.2313` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.8826` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0442` n `13`; crypto_alt avg `0.3099` n `239`; crypto_major avg `0.2105` n `8`; equity avg `0.0491` n `168`; fx avg `0.0042` n `6`; index avg `-0.0042` n `27`; metal avg `0.0646` n `20`; unknown avg `-0.3834` n `1265`
- 1h: commodity avg `-0.0001` n `13`; crypto_alt avg `-0.2912` n `239`; crypto_major avg `-0.3927` n `8`; equity avg `-0.1789` n `168`; fx avg `0.0041` n `6`; index avg `-0.0216` n `27`; metal avg `0.1617` n `20`; unknown avg `236.7024` n `1255`
- 4h: commodity avg `0.0869` n `13`; crypto_alt avg `3.5275` n `239`; crypto_major avg `3.0414` n `8`; equity avg `5.2727` n `168`; fx avg `0.0837` n `6`; index avg `0.5093` n `27`; metal avg `1.1588` n `20`; unknown avg `22.8713` n `1256`
- 24h: commodity avg `0.3973` n `13`; crypto_alt avg `2.5034` n `239`; crypto_major avg `1.4717` n `8`; equity avg `-0.4014` n `168`; fx avg `0.0524` n `6`; index avg `-0.0476` n `27`; metal avg `0.1803` n `20`; unknown avg `25.3056` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
