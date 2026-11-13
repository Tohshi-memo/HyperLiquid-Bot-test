# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T06:37:27.218020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2609` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.066` n `13`; crypto_alt avg `0.2146` n `239`; crypto_major avg `0.2243` n `8`; equity avg `-0.0327` n `162`; fx avg `-0.0154` n `6`; index avg `-0.0161` n `27`; metal avg `-0.0516` n `20`; unknown avg `0.0991` n `1260`
- 1h: commodity avg `0.0906` n `13`; crypto_alt avg `1.4738` n `239`; crypto_major avg `0.9453` n `8`; equity avg `0.0018` n `162`; fx avg `0.0155` n `6`; index avg `-0.0147` n `27`; metal avg `-0.1799` n `20`; unknown avg `162.6171` n `1230`
- 4h: commodity avg `-0.0618` n `13`; crypto_alt avg `-0.6144` n `239`; crypto_major avg `-1.4613` n `8`; equity avg `-1.5438` n `162`; fx avg `0.0264` n `6`; index avg `-0.2004` n `27`; metal avg `-0.262` n `20`; unknown avg `1.2232` n `1216`
- 24h: commodity avg `0.7454` n `13`; crypto_alt avg `-1.397` n `239`; crypto_major avg `-3.3806` n `8`; equity avg `-1.1748` n `162`; fx avg `0.0141` n `6`; index avg `0.0057` n `27`; metal avg `-0.581` n `20`; unknown avg `98.4907` n `1133`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
