# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T15:52:28.516254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.65` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.8745` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.845` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.4055` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.7208` n `233`; crypto_major avg `-0.7335` n `8`; equity avg `-0.0481` n `136`; fx avg `0.0052` n `6`; index avg `0.0098` n `26`; metal avg `-0.0181` n `20`; unknown avg `0.7357` n `796`
- 1h: commodity avg `0.015` n `12`; crypto_alt avg `-0.2163` n `233`; crypto_major avg `-0.4901` n `8`; equity avg `0.1448` n `136`; fx avg `0.0103` n `6`; index avg `0.0713` n `26`; metal avg `-0.1065` n `20`; unknown avg `0.9725` n `794`
- 4h: commodity avg `0.1322` n `12`; crypto_alt avg `3.0148` n `233`; crypto_major avg `3.0067` n `8`; equity avg `0.6012` n `136`; fx avg `-0.0174` n `6`; index avg `0.1301` n `26`; metal avg `0.1617` n `20`; unknown avg `0.9744` n `772`
- 24h: commodity avg `-0.2894` n `12`; crypto_alt avg `1.8379` n `233`; crypto_major avg `2.6896` n `8`; equity avg `0.24` n `136`; fx avg `-0.1513` n `6`; index avg `0.2946` n `26`; metal avg `0.0522` n `20`; unknown avg `2.4157` n `697`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
