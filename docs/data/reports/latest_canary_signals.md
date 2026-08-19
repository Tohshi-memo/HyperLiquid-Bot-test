# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T15:07:34.781421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.2444` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.7538` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1409` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.0275` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.0075` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0455` n `12`; crypto_alt avg `1.0431` n `230`; crypto_major avg `1.5321` n `8`; equity avg `0.3094` n `121`; fx avg `0.0237` n `6`; index avg `0.0497` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.1638` n `792`
- 1h: commodity avg `0.0939` n `12`; crypto_alt avg `1.4487` n `230`; crypto_major avg `2.1214` n `8`; equity avg `0.7552` n `121`; fx avg `0.008` n `6`; index avg `0.0791` n `25`; metal avg `0.1139` n `20`; unknown avg `-0.0645` n `792`
- 4h: commodity avg `0.1034` n `12`; crypto_alt avg `1.7737` n `230`; crypto_major avg `2.8572` n `8`; equity avg `-0.3872` n `120`; fx avg `0.0397` n `6`; index avg `0.0438` n `25`; metal avg `0.7163` n `20`; unknown avg `0.7934` n `792`
- 24h: commodity avg `0.4032` n `12`; crypto_alt avg `1.9787` n `230`; crypto_major avg `2.9643` n `8`; equity avg `-0.3255` n `120`; fx avg `-0.202` n `6`; index avg `0.0509` n `25`; metal avg `0.6341` n `20`; unknown avg `0.2231` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
