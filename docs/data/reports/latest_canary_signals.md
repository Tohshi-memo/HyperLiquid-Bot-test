# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T11:52:34.023013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8257` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6835` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2952` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0034` n `13`; crypto_alt avg `-0.0932` n `239`; crypto_major avg `-0.2359` n `8`; equity avg `-0.0464` n `162`; fx avg `-0.0077` n `6`; index avg `-0.0018` n `27`; metal avg `-0.0135` n `20`; unknown avg `0.2039` n `1263`
- 1h: commodity avg `-0.0015` n `13`; crypto_alt avg `0.0206` n `239`; crypto_major avg `0.1699` n `8`; equity avg `0.0179` n `162`; fx avg `-0.0087` n `6`; index avg `0.0029` n `27`; metal avg `0.0122` n `20`; unknown avg `0.5636` n `1261`
- 4h: commodity avg `-0.0293` n `13`; crypto_alt avg `1.6604` n `239`; crypto_major avg `2.7964` n `8`; equity avg `0.5012` n `162`; fx avg `-0.0279` n `6`; index avg `0.0265` n `27`; metal avg `0.1129` n `20`; unknown avg `0.7886` n `1245`
- 24h: commodity avg `0.0263` n `13`; crypto_alt avg `-3.9308` n `239`; crypto_major avg `-3.0987` n `8`; equity avg `-0.7181` n `162`; fx avg `0.0125` n `6`; index avg `-0.055` n `27`; metal avg `-0.3397` n `20`; unknown avg `-0.033` n `1136`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
