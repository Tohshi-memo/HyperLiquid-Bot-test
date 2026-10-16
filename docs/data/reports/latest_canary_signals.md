# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T15:52:29.343816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7908` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6907` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2389` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0875` n `13`; crypto_alt avg `-0.3804` n `236`; crypto_major avg `-0.3615` n `8`; equity avg `-0.0896` n `151`; fx avg `-0.0153` n `6`; index avg `-0.0183` n `26`; metal avg `-0.052` n `20`; unknown avg `-0.0731` n `1148`
- 1h: commodity avg `0.1634` n `13`; crypto_alt avg `-1.4598` n `236`; crypto_major avg `-1.3952` n `8`; equity avg `-0.8752` n `151`; fx avg `-0.0358` n `6`; index avg `-0.1563` n `26`; metal avg `-0.1748` n `20`; unknown avg `3.0608` n `1140`
- 4h: commodity avg `-0.2883` n `13`; crypto_alt avg `-1.8107` n `236`; crypto_major avg `-1.9359` n `8`; equity avg `-1.9102` n `151`; fx avg `-0.0142` n `6`; index avg `-0.2452` n `26`; metal avg `-0.1451` n `20`; unknown avg `3.5256` n `996`
- 24h: commodity avg `-0.3656` n `13`; crypto_alt avg `-0.5086` n `236`; crypto_major avg `-1.3106` n `8`; equity avg `-1.189` n `151`; fx avg `0.0111` n `6`; index avg `-0.1953` n `26`; metal avg `0.0974` n `20`; unknown avg `-0.1735` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1136`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0984`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0803`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.076`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0747`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `666`, weak_sample_signal
