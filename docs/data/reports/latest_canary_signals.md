# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T05:52:27.394282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.1757` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1613` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.1593` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.9995` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `-0.2062` n `230`; crypto_major avg `-0.3073` n `8`; equity avg `-0.0097` n `121`; fx avg `-0.0063` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0586` n `794`
- 1h: commodity avg `0.0056` n `12`; crypto_alt avg `0.0398` n `230`; crypto_major avg `-0.24` n `8`; equity avg `-0.065` n `121`; fx avg `-0.0162` n `6`; index avg `-0.009` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.2827` n `794`
- 4h: commodity avg `-0.0204` n `12`; crypto_alt avg `-2.4166` n `230`; crypto_major avg `-2.1797` n `8`; equity avg `-0.1802` n `121`; fx avg `-0.0008` n `6`; index avg `-0.004` n `25`; metal avg `-0.0184` n `20`; unknown avg `0.3` n `794`
- 24h: commodity avg `-0.0513` n `12`; crypto_alt avg `-4.5163` n `230`; crypto_major avg `-2.3712` n `8`; equity avg `-0.052` n `121`; fx avg `0.0685` n `6`; index avg `-0.0077` n `25`; metal avg `0.0288` n `20`; unknown avg `2.0236` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
