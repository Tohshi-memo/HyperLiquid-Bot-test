# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T04:07:27.058859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7197` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2909` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2496` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1539` n `13`; crypto_alt avg `0.0733` n `235`; crypto_major avg `0.0295` n `8`; equity avg `0.0894` n `151`; fx avg `-0.0098` n `6`; index avg `-0.008` n `26`; metal avg `0.0205` n `20`; unknown avg `-0.0086` n `1127`
- 1h: commodity avg `-0.0606` n `13`; crypto_alt avg `0.8273` n `235`; crypto_major avg `0.4759` n `8`; equity avg `0.5553` n `151`; fx avg `-0.009` n `6`; index avg `0.0464` n `26`; metal avg `0.117` n `20`; unknown avg `0.5704` n `1095`
- 4h: commodity avg `-0.2682` n `13`; crypto_alt avg `2.0332` n `235`; crypto_major avg `2.4515` n `8`; equity avg `0.2019` n `151`; fx avg `0.082` n `6`; index avg `-0.1225` n `26`; metal avg `0.1606` n `20`; unknown avg `1.9688` n `1095`
- 24h: commodity avg `0.4876` n `13`; crypto_alt avg `-4.1443` n `235`; crypto_major avg `-2.1002` n `8`; equity avg `-3.7173` n `151`; fx avg `0.0157` n `6`; index avg `-0.583` n `26`; metal avg `-0.1339` n `20`; unknown avg `0.5817` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2054`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1931`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1335`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1134`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0876`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0826`, n `666`, weak_sample_signal
