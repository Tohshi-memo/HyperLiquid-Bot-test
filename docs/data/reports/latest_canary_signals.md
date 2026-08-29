# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T09:07:27.373757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `-0.0069` n `231`; crypto_major avg `-0.0023` n `8`; equity avg `0.0226` n `127`; fx avg `-0.0003` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.0729` n `793`
- 1h: commodity avg `0.0213` n `12`; crypto_alt avg `-0.1128` n `231`; crypto_major avg `0.0151` n `8`; equity avg `-0.0212` n `127`; fx avg `-0.0025` n `6`; index avg `-0.0033` n `26`; metal avg `0.009` n `20`; unknown avg `-0.0318` n `793`
- 4h: commodity avg `0.0209` n `12`; crypto_alt avg `-0.7963` n `231`; crypto_major avg `-0.4867` n `8`; equity avg `0.0208` n `127`; fx avg `-0.0062` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.0602` n `761`
- 24h: commodity avg `-0.0741` n `12`; crypto_alt avg `-2.1336` n `231`; crypto_major avg `-2.3` n `8`; equity avg `-1.368` n `127`; fx avg `-0.0199` n `6`; index avg `-0.1381` n `26`; metal avg `-0.6387` n `20`; unknown avg `-0.3391` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
