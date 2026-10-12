# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T12:37:27.178278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2667` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0245` n `13`; crypto_alt avg `-0.5934` n `235`; crypto_major avg `-0.5366` n `8`; equity avg `-0.1726` n `151`; fx avg `-0.0001` n `6`; index avg `-0.0346` n `26`; metal avg `-0.0546` n `20`; unknown avg `2.8722` n `1134`
- 1h: commodity avg `0.0182` n `13`; crypto_alt avg `-0.4732` n `235`; crypto_major avg `-0.6671` n `8`; equity avg `-0.1109` n `151`; fx avg `-0.0129` n `6`; index avg `-0.0126` n `26`; metal avg `-0.1044` n `20`; unknown avg `2.2679` n `1126`
- 4h: commodity avg `0.3119` n `13`; crypto_alt avg `-1.5166` n `235`; crypto_major avg `-1.3637` n `8`; equity avg `-0.4934` n `151`; fx avg `-0.0037` n `6`; index avg `-0.097` n `26`; metal avg `-0.0838` n `20`; unknown avg `1.6871` n `1019`
- 24h: commodity avg `0.1028` n `13`; crypto_alt avg `0.6117` n `235`; crypto_major avg `0.1184` n `8`; equity avg `-1.49` n `151`; fx avg `-0.1258` n `6`; index avg `-0.1756` n `26`; metal avg `-0.0752` n `20`; unknown avg `0.6621` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2455`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
