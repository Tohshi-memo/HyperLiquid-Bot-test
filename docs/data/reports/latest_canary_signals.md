# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T03:07:28.440998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6664` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.0661` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0613` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0052` n `13`; crypto_alt avg `0.0707` n `236`; crypto_major avg `-0.0471` n `8`; equity avg `-0.0802` n `151`; fx avg `0.0036` n `6`; index avg `-0.0173` n `26`; metal avg `0.0117` n `20`; unknown avg `1.439` n `1134`
- 1h: commodity avg `-0.0258` n `13`; crypto_alt avg `-1.9011` n `236`; crypto_major avg `-1.1419` n `8`; equity avg `-0.2973` n `151`; fx avg `0.0339` n `6`; index avg `-0.0758` n `26`; metal avg `0.0817` n `20`; unknown avg `2.9431` n `1134`
- 4h: commodity avg `-0.2662` n `13`; crypto_alt avg `-2.7263` n `236`; crypto_major avg `-1.4046` n `8`; equity avg `-0.8147` n `151`; fx avg `0.2306` n `6`; index avg `-0.3433` n `26`; metal avg `0.2618` n `20`; unknown avg `3.2276` n `1128`
- 24h: commodity avg `-0.4717` n `13`; crypto_alt avg `-5.3297` n `236`; crypto_major avg `-3.9096` n `8`; equity avg `-6.2258` n `151`; fx avg `0.1099` n `6`; index avg `-1.0759` n `26`; metal avg `-0.679` n `20`; unknown avg `1397.8893` n `890`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1423`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1312`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1077`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.104`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0844`, n `666`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0778`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
