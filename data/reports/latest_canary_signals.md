# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T21:22:28.886194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6918` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5861` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `0.1396` n `228`; crypto_major avg `0.151` n `8`; equity avg `-0.1893` n `86`; fx avg `-0.003` n `6`; index avg `-0.0049` n `23`; metal avg `0.0109` n `20`; unknown avg `-0.5079` n `764`
- 1h: commodity avg `0.0439` n `12`; crypto_alt avg `0.012` n `228`; crypto_major avg `0.1257` n `8`; equity avg `0.3048` n `86`; fx avg `0.0016` n `6`; index avg `0.1226` n `23`; metal avg `0.0411` n `20`; unknown avg `-0.6937` n `764`
- 4h: commodity avg `-0.0539` n `12`; crypto_alt avg `3.0682` n `228`; crypto_major avg `2.6379` n `8`; equity avg `2.2507` n `86`; fx avg `-0.0053` n `6`; index avg `0.586` n `23`; metal avg `0.0518` n `20`; unknown avg `8.0722` n `764`
- 24h: commodity avg `-0.5277` n `12`; crypto_alt avg `-2.8956` n `228`; crypto_major avg `-2.1851` n `8`; equity avg `3.9624` n `86`; fx avg `0.0594` n `6`; index avg `0.5867` n `23`; metal avg `-1.6659` n `20`; unknown avg `-0.8164` n `724`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
