# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T15:37:30.044607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `4.5538` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `4.4991` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.8888` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `3.7251` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `3.624` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `3.5164` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `1.3376` n `230`; crypto_major avg `1.7068` n `8`; equity avg `0.005` n `121`; fx avg `0.005` n `6`; index avg `-0.017` n `25`; metal avg `0.0221` n `20`; unknown avg `-0.0042` n `792`
- 1h: commodity avg `0.1042` n `12`; crypto_alt avg `2.6269` n `230`; crypto_major avg `3.7282` n `8`; equity avg `0.2118` n `121`; fx avg `0.0406` n `6`; index avg `0.0004` n `25`; metal avg `0.0031` n `20`; unknown avg `0.1749` n `792`
- 4h: commodity avg `0.1163` n `12`; crypto_alt avg `3.0614` n `230`; crypto_major avg `4.6154` n `8`; equity avg `0.0616` n `120`; fx avg `0.0573` n `6`; index avg `0.0546` n `25`; metal avg `0.7266` n `20`; unknown avg `1.2216` n `792`
- 24h: commodity avg `0.296` n `12`; crypto_alt avg `3.056` n `230`; crypto_major avg `4.543` n `8`; equity avg `-0.2713` n `120`; fx avg `-0.1757` n `6`; index avg `0.0508` n `25`; metal avg `0.737` n `20`; unknown avg `0.4129` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
