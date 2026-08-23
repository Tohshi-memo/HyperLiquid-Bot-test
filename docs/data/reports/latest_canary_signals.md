# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T05:22:31.242058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.3295` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3049` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.2711` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.19` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `0.3589` n `230`; crypto_major avg `0.2198` n `8`; equity avg `-0.0175` n `121`; fx avg `0.0122` n `6`; index avg `0.0035` n `25`; metal avg `0.0115` n `20`; unknown avg `0.445` n `794`
- 1h: commodity avg `-0.0226` n `12`; crypto_alt avg `-0.237` n `230`; crypto_major avg `-0.482` n `8`; equity avg `-0.083` n `121`; fx avg `0.0139` n `6`; index avg `0.0003` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.2418` n `794`
- 4h: commodity avg `-0.049` n `12`; crypto_alt avg `-2.8957` n `230`; crypto_major avg `-2.3201` n `8`; equity avg `-0.1301` n `121`; fx avg `0.0286` n `6`; index avg `0.0094` n `25`; metal avg `-0.0152` n `20`; unknown avg `3.9089` n `794`
- 24h: commodity avg `-0.0225` n `12`; crypto_alt avg `-2.7308` n `230`; crypto_major avg `0.1521` n `8`; equity avg `0.2943` n `121`; fx avg `0.1086` n `6`; index avg `0.0176` n `25`; metal avg `0.1271` n `20`; unknown avg `2.6322` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
