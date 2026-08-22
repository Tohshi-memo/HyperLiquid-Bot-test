# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T04:22:24.983974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.7601` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.7468` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.7102` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `0.3341` n `230`; crypto_major avg `0.2524` n `8`; equity avg `-0.0245` n `121`; fx avg `0.0175` n `6`; index avg `-0.0033` n `25`; metal avg `-0.0323` n `20`; unknown avg `0.3424` n `794`
- 1h: commodity avg `0.0203` n `12`; crypto_alt avg `0.5615` n `230`; crypto_major avg `-0.0826` n `8`; equity avg `-0.0591` n `121`; fx avg `0.0172` n `6`; index avg `-0.0258` n `25`; metal avg `-0.0374` n `20`; unknown avg `0.7259` n `793`
- 4h: commodity avg `0.0054` n `12`; crypto_alt avg `3.9288` n `230`; crypto_major avg `3.7156` n `8`; equity avg `-0.0312` n `121`; fx avg `0.0394` n `6`; index avg `-0.0203` n `25`; metal avg `-0.0445` n `20`; unknown avg `1.1771` n `793`
- 24h: commodity avg `0.1221` n `12`; crypto_alt avg `12.1092` n `230`; crypto_major avg `9.842` n `8`; equity avg `0.3673` n `121`; fx avg `0.0649` n `6`; index avg `-0.0031` n `25`; metal avg `0.1392` n `20`; unknown avg `2.5316` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
