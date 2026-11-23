# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T17:37:42.910311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.8976` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.1913` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0054` n `13`; crypto_alt avg `-0.0925` n `239`; crypto_major avg `-0.2091` n `8`; equity avg `0.1429` n `166`; fx avg `-0.0083` n `6`; index avg `0.0202` n `27`; metal avg `-0.0007` n `20`; unknown avg `0.1052` n `1266`
- 1h: commodity avg `0.1889` n `13`; crypto_alt avg `-0.6247` n `239`; crypto_major avg `-0.6792` n `8`; equity avg `0.2504` n `166`; fx avg `-0.011` n `6`; index avg `0.033` n `27`; metal avg `-0.0704` n `20`; unknown avg `6.9486` n `1266`
- 4h: commodity avg `-0.3675` n `13`; crypto_alt avg `1.8861` n `239`; crypto_major avg `1.8238` n `8`; equity avg `4.7214` n `166`; fx avg `-0.1823` n `6`; index avg `0.558` n `27`; metal avg `0.5018` n `20`; unknown avg `326.872` n `1254`
- 24h: commodity avg `-1.3593` n `13`; crypto_alt avg `2.3817` n `239`; crypto_major avg `2.6621` n `8`; equity avg `6.3534` n `166`; fx avg `-0.0727` n `6`; index avg `0.5899` n `27`; metal avg `0.7228` n `20`; unknown avg `244.716` n `1061`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
