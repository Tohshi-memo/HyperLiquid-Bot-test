# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T18:37:26.592746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.4374` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.0863` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7802` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `0.0817` n `229`; crypto_major avg `0.1161` n `8`; equity avg `-0.1572` n `91`; fx avg `0.0132` n `6`; index avg `-0.006` n `25`; metal avg `0.0631` n `20`; unknown avg `-0.0399` n `763`
- 1h: commodity avg `0.0599` n `12`; crypto_alt avg `0.1604` n `229`; crypto_major avg `0.1511` n `8`; equity avg `-0.1963` n `91`; fx avg `0.0005` n `6`; index avg `0.0257` n `25`; metal avg `0.1219` n `20`; unknown avg `-0.0956` n `763`
- 4h: commodity avg `-0.0805` n `12`; crypto_alt avg `1.8075` n `229`; crypto_major avg `2.0058` n `8`; equity avg `-0.4316` n `90`; fx avg `0.0279` n `6`; index avg `-0.0402` n `25`; metal avg `0.2256` n `20`; unknown avg `1.6684` n `763`
- 24h: commodity avg `-0.0243` n `12`; crypto_alt avg `1.0609` n `229`; crypto_major avg `0.8445` n `8`; equity avg `-0.6616` n `90`; fx avg `0.2078` n `6`; index avg `0.02` n `25`; metal avg `-0.1052` n `20`; unknown avg `0.8177` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
