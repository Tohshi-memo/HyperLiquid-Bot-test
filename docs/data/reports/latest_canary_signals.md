# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T17:52:32.612928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.9654` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.7196` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.6326` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.043` n `13`; crypto_alt avg `0.1544` n `239`; crypto_major avg `0.0326` n `8`; equity avg `0.103` n `166`; fx avg `-0.0213` n `6`; index avg `-0.0116` n `27`; metal avg `-0.0191` n `20`; unknown avg `1.3209` n `1262`
- 1h: commodity avg `0.0383` n `13`; crypto_alt avg `-0.4257` n `239`; crypto_major avg `-0.835` n `8`; equity avg `-0.2677` n `166`; fx avg `-0.0097` n `6`; index avg `-0.0664` n `27`; metal avg `-0.1107` n `20`; unknown avg `2.0409` n `1255`
- 4h: commodity avg `-0.1121` n `13`; crypto_alt avg `-3.3842` n `239`; crypto_major avg `-4.0775` n `8`; equity avg `-3.3126` n `166`; fx avg `-0.0089` n `6`; index avg `-0.3579` n `27`; metal avg `-0.4449` n `20`; unknown avg `-0.3764` n `1247`
- 24h: commodity avg `-0.2987` n `13`; crypto_alt avg `-6.1377` n `239`; crypto_major avg `-6.8941` n `8`; equity avg `-8.7174` n `166`; fx avg `-0.0072` n `6`; index avg `-0.8198` n `27`; metal avg `-1.3081` n `20`; unknown avg `37.1934` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
