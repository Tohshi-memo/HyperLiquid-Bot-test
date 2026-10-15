# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T05:51:37.612610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.799` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7863` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.194` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0156` n `13`; crypto_alt avg `-0.6013` n `236`; crypto_major avg `-0.5183` n `8`; equity avg `-0.1388` n `151`; fx avg `-0.0099` n `6`; index avg `-0.015` n `26`; metal avg `0.0523` n `20`; unknown avg `1.336` n `1136`
- 1h: commodity avg `0.002` n `13`; crypto_alt avg `-1.6011` n `236`; crypto_major avg `-1.3241` n `8`; equity avg `-0.6696` n `151`; fx avg `0.0099` n `6`; index avg `-0.1301` n `26`; metal avg `0.0018` n `20`; unknown avg `0.9269` n `1134`
- 4h: commodity avg `0.0134` n `13`; crypto_alt avg `-3.1122` n `236`; crypto_major avg `-1.8517` n `8`; equity avg `-0.427` n `151`; fx avg `0.0198` n `6`; index avg `-0.0654` n `26`; metal avg `-0.0527` n `20`; unknown avg `0.9457` n `1128`
- 24h: commodity avg `-0.3757` n `13`; crypto_alt avg `-5.585` n `236`; crypto_major avg `-4.025` n `8`; equity avg `-5.7575` n `151`; fx avg `0.0736` n `6`; index avg `-0.9926` n `26`; metal avg `-0.6962` n `20`; unknown avg `1392.8767` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1076`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1018`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.093`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0871`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0841`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0747`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0608`, n `666`, weak_sample_signal
