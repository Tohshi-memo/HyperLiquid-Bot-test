# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T18:13:07.300335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.6487` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.4527` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.1555` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0683` n `12`; crypto_alt avg `-0.1448` n `230`; crypto_major avg `-0.2041` n `8`; equity avg `-0.2042` n `121`; fx avg `-0.0106` n `6`; index avg `-0.021` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.0693` n `792`
- 1h: commodity avg `-0.1828` n `12`; crypto_alt avg `-0.1663` n `230`; crypto_major avg `-0.0459` n `8`; equity avg `-0.2944` n `121`; fx avg `-0.0077` n `6`; index avg `-0.0456` n `25`; metal avg `-0.0076` n `20`; unknown avg `0.2494` n `792`
- 4h: commodity avg `-0.0003` n `12`; crypto_alt avg `2.0823` n `230`; crypto_major avg `3.6484` n `8`; equity avg `0.4929` n `121`; fx avg `0.0007` n `6`; index avg `-0.0276` n `25`; metal avg `0.1957` n `20`; unknown avg `0.1517` n `792`
- 24h: commodity avg `0.2366` n `12`; crypto_alt avg `2.6192` n `230`; crypto_major avg `4.598` n `8`; equity avg `-0.336` n `120`; fx avg `-0.2039` n `6`; index avg `-0.0059` n `25`; metal avg `0.8434` n `20`; unknown avg `0.4278` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1881`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
