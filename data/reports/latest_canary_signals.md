# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T15:07:35.038163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2843` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0521` n `13`; crypto_alt avg `0.1124` n `235`; crypto_major avg `0.1189` n `8`; equity avg `-0.075` n `151`; fx avg `-0.011` n `6`; index avg `0.0069` n `26`; metal avg `0.0103` n `20`; unknown avg `0.0405` n `1132`
- 1h: commodity avg `0.1138` n `13`; crypto_alt avg `-0.9791` n `235`; crypto_major avg `-0.7267` n `8`; equity avg `-0.2374` n `151`; fx avg `-0.0214` n `6`; index avg `-0.0026` n `26`; metal avg `-0.1058` n `20`; unknown avg `-0.4841` n `1080`
- 4h: commodity avg `0.4101` n `13`; crypto_alt avg `-1.858` n `235`; crypto_major avg `-1.3967` n `8`; equity avg `-1.6414` n `151`; fx avg `0.0065` n `6`; index avg `-0.1124` n `26`; metal avg `-0.123` n `20`; unknown avg `-0.2746` n `1073`
- 24h: commodity avg `0.5104` n `13`; crypto_alt avg `-1.3933` n `235`; crypto_major avg `-0.6804` n `8`; equity avg `-2.9963` n `151`; fx avg `-0.1264` n `6`; index avg `-0.2885` n `26`; metal avg `-0.1067` n `20`; unknown avg `-0.3542` n `881`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2451`, n `667`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2096`, n `667`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `667`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.121`, n `667`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1071`, n `667`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0958`, n `667`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0868`, n `667`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0794`, n `667`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
