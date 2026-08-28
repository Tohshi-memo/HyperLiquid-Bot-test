# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T17:52:25.111843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.488` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0451` n `12`; crypto_alt avg `0.1956` n `231`; crypto_major avg `0.2341` n `8`; equity avg `0.1028` n `127`; fx avg `-0.0015` n `6`; index avg `0.0165` n `26`; metal avg `-0.008` n `20`; unknown avg `6.9695` n `793`
- 1h: commodity avg `0.0197` n `12`; crypto_alt avg `-0.0733` n `231`; crypto_major avg `-0.2648` n `8`; equity avg `-0.0789` n `127`; fx avg `-0.0244` n `6`; index avg `-0.0314` n `26`; metal avg `-0.0611` n `20`; unknown avg `-0.0198` n `793`
- 4h: commodity avg `0.1605` n `12`; crypto_alt avg `-1.4938` n `231`; crypto_major avg `-1.6378` n `8`; equity avg `-1.2059` n `127`; fx avg `-0.0165` n `6`; index avg `-0.1498` n `26`; metal avg `-0.8348` n `20`; unknown avg `7.0193` n `793`
- 24h: commodity avg `-0.1847` n `12`; crypto_alt avg `-3.4167` n `231`; crypto_major avg `-3.3614` n `8`; equity avg `-2.0562` n `127`; fx avg `-0.1082` n `6`; index avg `-0.1214` n `26`; metal avg `-0.2256` n `20`; unknown avg `-0.3916` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
