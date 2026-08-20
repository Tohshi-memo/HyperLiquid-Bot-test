# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T16:02:48.873035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4485` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.3013` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6795` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0423` n `12`; crypto_alt avg `0.0161` n `230`; crypto_major avg `0.0081` n `8`; equity avg `0.0335` n `121`; fx avg `-0.0081` n `6`; index avg `0.0268` n `25`; metal avg `0.0295` n `20`; unknown avg `-0.0492` n `792`
- 1h: commodity avg `0.0359` n `12`; crypto_alt avg `0.3209` n `230`; crypto_major avg `0.8055` n `8`; equity avg `-0.2813` n `121`; fx avg `0.0139` n `6`; index avg `-0.0456` n `25`; metal avg `0.013` n `20`; unknown avg `-0.0878` n `792`
- 4h: commodity avg `-0.1798` n `12`; crypto_alt avg `1.3613` n `230`; crypto_major avg `2.2687` n `8`; equity avg `-0.0326` n `121`; fx avg `-0.0184` n `6`; index avg `0.0896` n `25`; metal avg `0.5892` n `20`; unknown avg `0.0228` n `792`
- 24h: commodity avg `-0.0554` n `12`; crypto_alt avg `6.1081` n `230`; crypto_major avg `9.1901` n `8`; equity avg `-0.8858` n `121`; fx avg `0.1543` n `6`; index avg `-0.0801` n `25`; metal avg `0.3125` n `20`; unknown avg `2.112` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
