# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T19:52:28.314408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4166` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.1775` n `231`; crypto_major avg `-0.1676` n `8`; equity avg `0.0082` n `127`; fx avg `-0.0011` n `6`; index avg `-0.0055` n `26`; metal avg `-0.063` n `20`; unknown avg `-0.1868` n `793`
- 1h: commodity avg `0.0354` n `12`; crypto_alt avg `0.6224` n `231`; crypto_major avg `0.5571` n `8`; equity avg `0.2069` n `127`; fx avg `-0.003` n `6`; index avg `0.021` n `26`; metal avg `-0.0024` n `20`; unknown avg `1.1678` n `793`
- 4h: commodity avg `0.0695` n `12`; crypto_alt avg `-1.3713` n `231`; crypto_major avg `-1.5458` n `8`; equity avg `-0.5505` n `127`; fx avg `-0.0349` n `6`; index avg `-0.1292` n `26`; metal avg `-0.6386` n `20`; unknown avg `-0.0258` n `793`
- 24h: commodity avg `-0.1421` n `12`; crypto_alt avg `-3.4761` n `231`; crypto_major avg `-3.7652` n `8`; equity avg `-2.3875` n `127`; fx avg `-0.1127` n `6`; index avg `-0.175` n `26`; metal avg `-0.4251` n `20`; unknown avg `-0.683` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
