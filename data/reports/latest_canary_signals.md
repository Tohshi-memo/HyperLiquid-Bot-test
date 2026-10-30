# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T05:37:31.602161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7361` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.638` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.931` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0379` n `13`; crypto_alt avg `0.138` n `238`; crypto_major avg `0.0941` n `8`; equity avg `-0.0514` n `156`; fx avg `0.0028` n `6`; index avg `-0.018` n `27`; metal avg `0.0861` n `20`; unknown avg `-0.1108` n `1258`
- 1h: commodity avg `-0.0133` n `13`; crypto_alt avg `0.824` n `238`; crypto_major avg `0.5362` n `8`; equity avg `-0.2097` n `156`; fx avg `-0.0001` n `6`; index avg `-0.0451` n `27`; metal avg `0.1152` n `20`; unknown avg `0.2386` n `1252`
- 4h: commodity avg `-0.0488` n `13`; crypto_alt avg `2.6039` n `238`; crypto_major avg `2.6873` n `8`; equity avg `0.7563` n `156`; fx avg `-0.0488` n `6`; index avg `0.069` n `27`; metal avg `0.0493` n `20`; unknown avg `9.6002` n `1232`
- 24h: commodity avg `-0.0192` n `13`; crypto_alt avg `-3.858` n `238`; crypto_major avg `-0.1551` n `8`; equity avg `-3.0726` n `155`; fx avg `0.1122` n `6`; index avg `-0.4261` n `27`; metal avg `-0.5625` n `20`; unknown avg `29.4171` n `980`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
