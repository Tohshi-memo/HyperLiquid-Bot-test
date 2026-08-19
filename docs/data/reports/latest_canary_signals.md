# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T16:22:36.221217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.7847` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `4.609` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `4.1026` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.8357` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.6045` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.1347` n `230`; crypto_major avg `-0.0685` n `8`; equity avg `-0.0563` n `121`; fx avg `0.0077` n `6`; index avg `-0.0142` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0232` n `792`
- 1h: commodity avg `0.0042` n `12`; crypto_alt avg `0.9578` n `230`; crypto_major avg `1.9861` n `8`; equity avg `0.3816` n `121`; fx avg `0.0074` n `6`; index avg `0.0035` n `25`; metal avg `0.1504` n `20`; unknown avg `0.1241` n `792`
- 4h: commodity avg `0.1216` n `12`; crypto_alt avg `2.6105` n `230`; crypto_major avg `4.9063` n `8`; equity avg `0.2973` n `120`; fx avg `0.0788` n `6`; index avg `0.0345` n `25`; metal avg `0.8037` n `20`; unknown avg `1.3501` n `792`
- 24h: commodity avg `0.3457` n `12`; crypto_alt avg `2.7634` n `230`; crypto_major avg `5.1983` n `8`; equity avg `-0.0221` n `120`; fx avg `-0.1706` n `6`; index avg `0.0649` n `25`; metal avg `0.8227` n `20`; unknown avg `0.4856` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
