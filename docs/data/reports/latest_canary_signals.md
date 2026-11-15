# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T14:52:23.472673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1916` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0079` n `13`; crypto_alt avg `-0.2376` n `239`; crypto_major avg `-0.1542` n `8`; equity avg `-0.0489` n `162`; fx avg `0.0028` n `6`; index avg `0.008` n `27`; metal avg `0.0049` n `20`; unknown avg `0.9593` n `1264`
- 1h: commodity avg `-0.0378` n `13`; crypto_alt avg `-1.1871` n `239`; crypto_major avg `-1.1965` n `8`; equity avg `-0.283` n `162`; fx avg `-0.0044` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0281` n `20`; unknown avg `0.983` n `1262`
- 4h: commodity avg `-0.0988` n `13`; crypto_alt avg `-0.8788` n `239`; crypto_major avg `-0.7363` n `8`; equity avg `-0.2333` n `162`; fx avg `-0.0226` n `6`; index avg `-0.0013` n `27`; metal avg `-0.006` n `20`; unknown avg `0.9416` n `1253`
- 24h: commodity avg `-0.0323` n `13`; crypto_alt avg `-2.5449` n `239`; crypto_major avg `-1.6796` n `8`; equity avg `-0.4357` n `162`; fx avg `-0.0166` n `6`; index avg `-0.0138` n `27`; metal avg `-0.2814` n `20`; unknown avg `0.1528` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
