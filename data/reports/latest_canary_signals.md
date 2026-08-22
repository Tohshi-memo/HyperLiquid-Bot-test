# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T03:37:30.743190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.6656` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.6259` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.5312` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.9303` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.8721` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `0.1071` n `230`; crypto_major avg `0.0128` n `8`; equity avg `0.0075` n `121`; fx avg `0.0022` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0252` n `793`
- 1h: commodity avg `-0.0129` n `12`; crypto_alt avg `1.5091` n `230`; crypto_major avg `1.9358` n `8`; equity avg `0.0637` n `121`; fx avg `0.0058` n `6`; index avg `0.0077` n `25`; metal avg `0.0055` n `20`; unknown avg `2.0657` n `793`
- 4h: commodity avg `-0.0574` n `12`; crypto_alt avg `3.8654` n `230`; crypto_major avg `3.6082` n `8`; equity avg `0.077` n `121`; fx avg `0.0263` n `6`; index avg `0.0069` n `25`; metal avg `-0.0177` n `20`; unknown avg `0.1755` n `793`
- 24h: commodity avg `0.0765` n `12`; crypto_alt avg `11.7383` n `230`; crypto_major avg `10.1871` n `8`; equity avg `0.2745` n `121`; fx avg `0.0239` n `6`; index avg `-0.0114` n `25`; metal avg `0.2542` n `20`; unknown avg `1.6327` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
