# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T04:37:24.674887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.6032` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0438` n `13`; crypto_alt avg `-0.2456` n `237`; crypto_major avg `-0.1695` n `8`; equity avg `-0.0065` n `151`; fx avg `-0.0036` n `6`; index avg `-0.0153` n `26`; metal avg `0.0049` n `20`; unknown avg `-0.108` n `1201`
- 1h: commodity avg `0.0223` n `13`; crypto_alt avg `-0.0339` n `237`; crypto_major avg `0.057` n `8`; equity avg `-0.1997` n `151`; fx avg `-0.0108` n `6`; index avg `-0.0556` n `26`; metal avg `-0.0143` n `20`; unknown avg `2.9838` n `1185`
- 4h: commodity avg `0.1466` n `13`; crypto_alt avg `-2.1558` n `237`; crypto_major avg `-1.844` n `8`; equity avg `-1.5623` n `151`; fx avg `-0.0577` n `6`; index avg `-0.2408` n `26`; metal avg `-0.4984` n `20`; unknown avg `7.6141` n `1177`
- 24h: commodity avg `-0.5261` n `13`; crypto_alt avg `-0.6761` n `237`; crypto_major avg `-0.5577` n `8`; equity avg `-2.0702` n `151`; fx avg `-0.011` n `6`; index avg `-0.3092` n `26`; metal avg `-0.514` n `20`; unknown avg `118.5221` n `930`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
