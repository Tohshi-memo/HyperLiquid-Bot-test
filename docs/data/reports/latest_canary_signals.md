# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T09:07:28.583349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.67` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0628` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0194` n `13`; crypto_alt avg `-0.0619` n `237`; crypto_major avg `-0.1154` n `8`; equity avg `-0.1478` n `151`; fx avg `-0.0013` n `6`; index avg `-0.0176` n `26`; metal avg `-0.0305` n `20`; unknown avg `14.3091` n `1191`
- 1h: commodity avg `-0.0644` n `13`; crypto_alt avg `-0.4333` n `237`; crypto_major avg `-0.4475` n `8`; equity avg `-0.1019` n `151`; fx avg `-0.006` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0347` n `20`; unknown avg `54.2001` n `1177`
- 4h: commodity avg `0.1559` n `13`; crypto_alt avg `-1.667` n `237`; crypto_major avg `-1.2014` n `8`; equity avg `-0.8173` n `151`; fx avg `-0.091` n `6`; index avg `-0.1386` n `26`; metal avg `-0.1599` n `20`; unknown avg `4.1585` n `1139`
- 24h: commodity avg `-0.1729` n `13`; crypto_alt avg `-2.8017` n `237`; crypto_major avg `-2.1447` n `8`; equity avg `-2.5408` n `151`; fx avg `-0.119` n `6`; index avg `-0.4127` n `26`; metal avg `-0.6405` n `20`; unknown avg `31.3273` n `926`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
