# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T06:52:30.290545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5809` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8412` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7699` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0502` n `12`; crypto_alt avg `0.3878` n `228`; crypto_major avg `0.2608` n `8`; equity avg `0.1846` n `86`; fx avg `0.0173` n `6`; index avg `0.0145` n `23`; metal avg `0.1647` n `20`; unknown avg `24.6091` n `765`
- 1h: commodity avg `-0.0901` n `12`; crypto_alt avg `0.7238` n `228`; crypto_major avg `0.9307` n `8`; equity avg `0.4865` n `86`; fx avg `-0.0471` n `6`; index avg `0.1062` n `23`; metal avg `0.442` n `20`; unknown avg `-0.0089` n `741`
- 4h: commodity avg `0.0244` n `12`; crypto_alt avg `2.2624` n `228`; crypto_major avg `2.6053` n `8`; equity avg `0.8354` n `86`; fx avg `-0.0784` n `6`; index avg `0.1407` n `23`; metal avg `0.7641` n `20`; unknown avg `0.2455` n `725`
- 24h: commodity avg `0.3491` n `12`; crypto_alt avg `-1.9901` n `228`; crypto_major avg `-2.185` n `8`; equity avg `-3.6605` n `86`; fx avg `0.0107` n `6`; index avg `-0.5398` n `23`; metal avg `0.6672` n `20`; unknown avg `0.8757` n `693`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2214`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
