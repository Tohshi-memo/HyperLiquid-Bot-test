# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T17:37:41.544289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.9384` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.6124` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.4244` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0391` n `12`; crypto_alt avg `0.0181` n `230`; crypto_major avg `0.0722` n `8`; equity avg `-0.0672` n `121`; fx avg `-0.005` n `6`; index avg `-0.0039` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.0968` n `792`
- 1h: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.348` n `230`; crypto_major avg `-0.6733` n `8`; equity avg `-0.662` n `121`; fx avg `-0.0098` n `6`; index avg `-0.0622` n `25`; metal avg `-0.0619` n `20`; unknown avg `-0.0338` n `792`
- 4h: commodity avg `0.0628` n `12`; crypto_alt avg `2.1939` n `230`; crypto_major avg `3.6752` n `8`; equity avg `-0.2632` n `121`; fx avg `0.0091` n `6`; index avg `-0.1177` n `25`; metal avg `0.2508` n `20`; unknown avg `0.5518` n `792`
- 24h: commodity avg `0.3261` n `12`; crypto_alt avg `2.498` n `230`; crypto_major avg `4.4539` n `8`; equity avg `-0.6304` n `120`; fx avg `-0.1908` n `6`; index avg `-0.0387` n `25`; metal avg `0.776` n `20`; unknown avg `0.4504` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
