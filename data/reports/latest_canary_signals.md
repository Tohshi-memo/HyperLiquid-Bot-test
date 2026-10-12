# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T15:52:25.599963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0186` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0576` n `13`; crypto_alt avg `-0.1187` n `235`; crypto_major avg `-0.0346` n `8`; equity avg `0.1105` n `151`; fx avg `-0.0135` n `6`; index avg `0.0116` n `26`; metal avg `0.0076` n `20`; unknown avg `1.5744` n `1134`
- 1h: commodity avg `0.0794` n `13`; crypto_alt avg `0.069` n `235`; crypto_major avg `0.1903` n `8`; equity avg `0.0271` n `151`; fx avg `-0.0444` n `6`; index avg `0.0412` n `26`; metal avg `0.0117` n `20`; unknown avg `2.3489` n `1132`
- 4h: commodity avg `0.3426` n `13`; crypto_alt avg `-1.5749` n `235`; crypto_major avg `-1.1104` n `8`; equity avg `-1.5445` n `151`; fx avg `-0.0304` n `6`; index avg `-0.0918` n `26`; metal avg `-0.129` n `20`; unknown avg `-0.0139` n `1074`
- 24h: commodity avg `0.488` n `13`; crypto_alt avg `-2.0604` n `235`; crypto_major avg `-1.2539` n `8`; equity avg `-2.9887` n `151`; fx avg `-0.1561` n `6`; index avg `-0.2664` n `26`; metal avg `-0.1173` n `20`; unknown avg `-0.4202` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2186`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2141`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1085`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1016`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0969`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.089`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
