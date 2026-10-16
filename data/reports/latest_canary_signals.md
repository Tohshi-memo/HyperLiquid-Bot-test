# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T15:07:33.591508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2108` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0113` n `13`; crypto_alt avg `-1.2658` n `236`; crypto_major avg `-1.0726` n `8`; equity avg `-0.7463` n `151`; fx avg `-0.0059` n `6`; index avg `-0.1126` n `26`; metal avg `-0.0443` n `20`; unknown avg `3.7647` n `1140`
- 1h: commodity avg `-0.0711` n `13`; crypto_alt avg `-0.7006` n `236`; crypto_major avg `-0.6836` n `8`; equity avg `-0.5567` n `151`; fx avg `-0.0002` n `6`; index avg `-0.0504` n `26`; metal avg `0.0429` n `20`; unknown avg `4.605` n `1050`
- 4h: commodity avg `-0.3963` n `13`; crypto_alt avg `-1.2888` n `236`; crypto_major avg `-1.444` n `8`; equity avg `-1.9976` n `151`; fx avg `0.0254` n `6`; index avg `-0.2332` n `26`; metal avg `-0.0056` n `20`; unknown avg `2.7611` n `998`
- 24h: commodity avg `-0.4874` n `13`; crypto_alt avg `0.4224` n `236`; crypto_major avg `-0.4114` n `8`; equity avg `-0.7706` n `151`; fx avg `0.0616` n `6`; index avg `-0.151` n `26`; metal avg `0.2501` n `20`; unknown avg `35.4293` n `908`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.103`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1003`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0848`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0841`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0838`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
