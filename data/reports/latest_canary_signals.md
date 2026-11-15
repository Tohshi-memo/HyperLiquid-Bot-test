# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T16:37:30.477285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3275` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0266` n `13`; crypto_alt avg `0.0296` n `239`; crypto_major avg `0.1166` n `8`; equity avg `0.2101` n `162`; fx avg `-0.003` n `6`; index avg `0.0131` n `27`; metal avg `0.0095` n `20`; unknown avg `6.2982` n `1265`
- 1h: commodity avg `0.0153` n `13`; crypto_alt avg `0.0604` n `239`; crypto_major avg `-0.0636` n `8`; equity avg `0.3098` n `162`; fx avg `0.0002` n `6`; index avg `0.0273` n `27`; metal avg `0.0226` n `20`; unknown avg `4.1805` n `1256`
- 4h: commodity avg `-0.0628` n `13`; crypto_alt avg `-1.19` n `239`; crypto_major avg `-1.2873` n `8`; equity avg `0.0939` n `162`; fx avg `-0.0227` n `6`; index avg `0.0402` n `27`; metal avg `-0.0145` n `20`; unknown avg `163.9862` n `1255`
- 24h: commodity avg `0.0548` n `13`; crypto_alt avg `-1.041` n `239`; crypto_major avg `-0.734` n `8`; equity avg `0.4039` n `162`; fx avg `-0.0122` n `6`; index avg `0.0782` n `27`; metal avg `-0.1215` n `20`; unknown avg `4.6097` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
