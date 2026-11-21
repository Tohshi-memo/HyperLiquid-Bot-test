# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T09:07:23.011993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7203` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5756` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9993` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.017` n `13`; crypto_alt avg `0.4175` n `239`; crypto_major avg `0.1425` n `8`; equity avg `-0.1414` n `166`; fx avg `-0.0046` n `6`; index avg `-0.0181` n `27`; metal avg `0.0062` n `20`; unknown avg `0.4309` n `1252`
- 1h: commodity avg `0.0315` n `13`; crypto_alt avg `0.1754` n `239`; crypto_major avg `0.3563` n `8`; equity avg `-0.1036` n `166`; fx avg `0.0284` n `6`; index avg `-0.0144` n `27`; metal avg `0.0319` n `20`; unknown avg `159.7629` n `1256`
- 4h: commodity avg `-0.016` n `13`; crypto_alt avg `1.5808` n `239`; crypto_major avg `2.7043` n `8`; equity avg `0.705` n `166`; fx avg `-0.0539` n `6`; index avg `0.0642` n `27`; metal avg `0.1287` n `20`; unknown avg `332.0557` n `1206`
- 24h: commodity avg `0.7551` n `13`; crypto_alt avg `-5.75` n `239`; crypto_major avg `-6.3711` n `8`; equity avg `-4.8338` n `166`; fx avg `-0.058` n `6`; index avg `-0.5621` n `27`; metal avg `-0.3619` n `20`; unknown avg `8.7618` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
