# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T04:07:36.711025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1265` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0045` n `13`; crypto_alt avg `0.2007` n `239`; crypto_major avg `0.22` n `8`; equity avg `0.0183` n `166`; fx avg `-0.0013` n `6`; index avg `0.0099` n `27`; metal avg `0.0153` n `20`; unknown avg `159.5861` n `1253`
- 1h: commodity avg `-0.0437` n `13`; crypto_alt avg `0.1744` n `239`; crypto_major avg `0.0026` n `8`; equity avg `-0.057` n `166`; fx avg `0.001` n `6`; index avg `0.012` n `27`; metal avg `-0.0321` n `20`; unknown avg `271.0251` n `1257`
- 4h: commodity avg `-0.0877` n `13`; crypto_alt avg `-0.953` n `239`; crypto_major avg `-1.1951` n `8`; equity avg `-0.4446` n `166`; fx avg `-0.0082` n `6`; index avg `-0.0686` n `27`; metal avg `-0.123` n `20`; unknown avg `1.2196` n `1257`
- 24h: commodity avg `0.0174` n `13`; crypto_alt avg `4.0756` n `239`; crypto_major avg `5.8641` n `8`; equity avg `1.7955` n `166`; fx avg `-0.0136` n `6`; index avg `0.2435` n `27`; metal avg `0.251` n `20`; unknown avg `761.3502` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
