# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T04:52:28.229591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0131` n `12`; crypto_alt avg `0.1044` n `231`; crypto_major avg `0.0959` n `8`; equity avg `-0.0027` n `127`; fx avg `0.0006` n `6`; index avg `0.0026` n `26`; metal avg `-0.0094` n `20`; unknown avg `0.353` n `793`
- 1h: commodity avg `0.0054` n `12`; crypto_alt avg `0.2503` n `231`; crypto_major avg `0.1575` n `8`; equity avg `0.0339` n `127`; fx avg `0.0138` n `6`; index avg `0.0159` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.2565` n `793`
- 4h: commodity avg `0.0042` n `12`; crypto_alt avg `-0.0113` n `231`; crypto_major avg `0.2083` n `8`; equity avg `0.1136` n `127`; fx avg `0.0157` n `6`; index avg `0.058` n `26`; metal avg `-0.004` n `20`; unknown avg `-0.1556` n `793`
- 24h: commodity avg `-0.1213` n `12`; crypto_alt avg `-1.6279` n `231`; crypto_major avg `-2.2015` n `8`; equity avg `-1.8025` n `127`; fx avg `-0.0684` n `6`; index avg `-0.1677` n `26`; metal avg `-0.2454` n `20`; unknown avg `-0.342` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
