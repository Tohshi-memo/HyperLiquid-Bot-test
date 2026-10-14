# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T14:37:26.743785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8427` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5547` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.4804` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.1778` n `235`; crypto_major avg `-0.21` n `8`; equity avg `-0.0147` n `151`; fx avg `0.0081` n `6`; index avg `-0.0014` n `26`; metal avg `0.0173` n `20`; unknown avg `0.0229` n `1136`
- 1h: commodity avg `-0.1106` n `13`; crypto_alt avg `-1.4896` n `235`; crypto_major avg `-1.5343` n `8`; equity avg `-0.384` n `151`; fx avg `-0.0275` n `6`; index avg `-0.0539` n `26`; metal avg `-0.1976` n `20`; unknown avg `-0.0906` n `1108`
- 4h: commodity avg `-0.3297` n `13`; crypto_alt avg `-2.2164` n `235`; crypto_major avg `-2.1015` n `8`; equity avg `-2.0359` n `151`; fx avg `-0.0971` n `6`; index avg `-0.2588` n `26`; metal avg `-0.5468` n `20`; unknown avg `3.3992` n `1102`
- 24h: commodity avg `0.113` n `13`; crypto_alt avg `-2.9246` n `235`; crypto_major avg `-2.4367` n `8`; equity avg `-2.1432` n `151`; fx avg `-0.1342` n `6`; index avg `-0.2705` n `26`; metal avg `-0.7009` n `20`; unknown avg `1262.9669` n `981`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1116`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1033`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0763`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0635`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
