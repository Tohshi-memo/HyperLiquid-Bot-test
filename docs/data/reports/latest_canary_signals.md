# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T01:52:27.482655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `2.2774` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.2578` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.2193` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0602` n `13`; crypto_alt avg `0.1851` n `235`; crypto_major avg `0.2578` n `8`; equity avg `0.0072` n `151`; fx avg `-0.0093` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0134` n `20`; unknown avg `0.2011` n `1135`
- 1h: commodity avg `-0.0737` n `13`; crypto_alt avg `2.5509` n `235`; crypto_major avg `2.1841` n `8`; equity avg `-0.0933` n `151`; fx avg `0.0391` n `6`; index avg `-0.0897` n `26`; metal avg `-0.0352` n `20`; unknown avg `4.6689` n `1133`
- 4h: commodity avg `-0.0632` n `13`; crypto_alt avg `-1.4811` n `235`; crypto_major avg `-0.9258` n `8`; equity avg `-1.2975` n `151`; fx avg `0.0512` n `6`; index avg `-0.2715` n `26`; metal avg `-0.171` n `20`; unknown avg `2.4584` n `1111`
- 24h: commodity avg `0.6922` n `13`; crypto_alt avg `-4.9239` n `235`; crypto_major avg `-3.1041` n `8`; equity avg `-4.7002` n `151`; fx avg `-0.0658` n `6`; index avg `-0.6087` n `26`; metal avg `-0.4226` n `20`; unknown avg `0.4097` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2101`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1909`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1219`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1099`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1053`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0867`, n `666`, weak_sample_signal
