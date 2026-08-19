# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T17:07:28.102050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `5.2122` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.7627` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.5187` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0249` n `12`; crypto_alt avg `-0.1981` n `230`; crypto_major avg `-0.3156` n `8`; equity avg `-0.2228` n `121`; fx avg `0.0055` n `6`; index avg `-0.01` n `25`; metal avg `-0.0392` n `20`; unknown avg `0.0475` n `792`
- 1h: commodity avg `0.0559` n `12`; crypto_alt avg `0.0698` n `230`; crypto_major avg `-0.4649` n `8`; equity avg `-0.4236` n `121`; fx avg `-0.012` n `6`; index avg `-0.0677` n `25`; metal avg `-0.0299` n `20`; unknown avg `-0.2056` n `792`
- 4h: commodity avg `0.2125` n `12`; crypto_alt avg `2.4045` n `230`; crypto_major avg `3.9752` n `8`; equity avg `-1.237` n `120`; fx avg `0.0495` n `6`; index avg `-0.1674` n `25`; metal avg `0.4565` n `20`; unknown avg `1.1709` n `792`
- 24h: commodity avg `0.4265` n `12`; crypto_alt avg `2.7402` n `230`; crypto_major avg `4.7044` n `8`; equity avg `-0.5353` n `120`; fx avg `-0.1834` n `6`; index avg `-0.0232` n `25`; metal avg `0.7863` n `20`; unknown avg `0.4916` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
