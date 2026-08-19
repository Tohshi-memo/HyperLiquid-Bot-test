# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T18:07:25.950015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.5667` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.423` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.0717` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `-0.1038` n `230`; crypto_major avg `-0.2261` n `8`; equity avg `-0.1448` n `121`; fx avg `-0.0072` n `6`; index avg `-0.0263` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.0657` n `792`
- 1h: commodity avg `-0.1241` n `12`; crypto_alt avg `-0.1255` n `230`; crypto_major avg `-0.0679` n `8`; equity avg `-0.2354` n `121`; fx avg `-0.0043` n `6`; index avg `-0.0509` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.2519` n `792`
- 4h: commodity avg `0.0589` n `12`; crypto_alt avg `2.1239` n `230`; crypto_major avg `3.6256` n `8`; equity avg `0.5539` n `121`; fx avg `0.0041` n `6`; index avg `-0.0329` n `25`; metal avg `0.2026` n `20`; unknown avg `0.1636` n `792`
- 24h: commodity avg `0.2963` n `12`; crypto_alt avg `2.6624` n `230`; crypto_major avg `4.5751` n `8`; equity avg `-0.2946` n `120`; fx avg `-0.2007` n `6`; index avg `-0.0112` n `25`; metal avg `0.8506` n `20`; unknown avg `0.44` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
