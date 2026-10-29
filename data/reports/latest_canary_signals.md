# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T03:22:31.645552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.018` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8489` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7264` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `-0.2855` n `238`; crypto_major avg `-0.1757` n `8`; equity avg `-0.191` n `155`; fx avg `0.0088` n `6`; index avg `-0.0425` n `27`; metal avg `-0.0817` n `20`; unknown avg `0.1238` n `1238`
- 1h: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.4712` n `238`; crypto_major avg `-0.1588` n `8`; equity avg `-0.1445` n `155`; fx avg `-0.004` n `6`; index avg `-0.0146` n `27`; metal avg `-0.1864` n `20`; unknown avg `1.2897` n `1222`
- 4h: commodity avg `-0.0253` n `13`; crypto_alt avg `-2.7419` n `238`; crypto_major avg `-2.0433` n `8`; equity avg `-1.3015` n `155`; fx avg `-0.1056` n `6`; index avg `-0.1944` n `27`; metal avg `-0.3169` n `20`; unknown avg `2.6927` n `1200`
- 24h: commodity avg `-0.051` n `13`; crypto_alt avg `-2.6276` n `238`; crypto_major avg `-1.8507` n `8`; equity avg `-1.5178` n `154`; fx avg `-0.0024` n `6`; index avg `-0.1909` n `27`; metal avg `-0.3293` n `20`; unknown avg `28.8609` n `986`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
