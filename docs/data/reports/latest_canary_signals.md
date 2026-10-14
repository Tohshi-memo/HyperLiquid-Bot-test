# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T13:22:27.224514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3605` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0995` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0103` n `13`; crypto_alt avg `-0.5764` n `235`; crypto_major avg `-0.478` n `8`; equity avg `-0.1147` n `151`; fx avg `0.0066` n `6`; index avg `-0.0071` n `26`; metal avg `-0.0472` n `20`; unknown avg `33.1951` n `1136`
- 1h: commodity avg `-0.0966` n `13`; crypto_alt avg `-1.8814` n `235`; crypto_major avg `-1.6342` n `8`; equity avg `-1.4398` n `151`; fx avg `-0.1` n `6`; index avg `-0.2737` n `26`; metal avg `-0.5525` n `20`; unknown avg `2.9031` n `1134`
- 4h: commodity avg `-0.0743` n `13`; crypto_alt avg `-2.022` n `235`; crypto_major avg `-1.3706` n `8`; equity avg `-1.5589` n `151`; fx avg `-0.0806` n `6`; index avg `-0.2711` n `26`; metal avg `-0.4555` n `20`; unknown avg `1.6196` n `1127`
- 24h: commodity avg `0.5778` n `13`; crypto_alt avg `-2.2583` n `235`; crypto_major avg `-1.2635` n `8`; equity avg `-1.0602` n `151`; fx avg `-0.1135` n `6`; index avg `-0.1785` n `26`; metal avg `-0.7893` n `20`; unknown avg `1263.8945` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1436`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1192`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0981`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0647`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
