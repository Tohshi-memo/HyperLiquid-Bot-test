# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T22:37:15.868366+00:00`
- Correlation status: `ready`
- Asset price records: `494`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.76` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0936` n `12`; crypto_alt avg `0.0218` n `228`; crypto_major avg `0.0165` n `8`; equity avg `0.0255` n `65`; fx avg `0.0011` n `4`; index avg `-0.0488` n `23`; metal avg `-0.0201` n `18`; unknown avg `-0.2403` n `356`
- 1h: commodity avg `-0.0924` n `12`; crypto_alt avg `-0.4604` n `228`; crypto_major avg `-0.3156` n `8`; equity avg `0.0684` n `65`; fx avg `0.0106` n `4`; index avg `-0.0675` n `23`; metal avg `0.0082` n `18`; unknown avg `-0.0357` n `356`
- 4h: commodity avg `0.3726` n `12`; crypto_alt avg `0.1831` n `228`; crypto_major avg `-0.063` n `8`; equity avg `-0.1524` n `65`; fx avg `-0.0063` n `4`; index avg `-0.0071` n `23`; metal avg `0.2041` n `18`; unknown avg `0.1902` n `356`
- 24h: commodity avg `-2.2194` n `7`; crypto_alt avg `1.735` n `223`; crypto_major avg `-0.3075` n `7`; equity avg `1.8723` n `47`; fx avg `-0.6086` n `4`; index avg `1.4379` n `6`; metal avg `3.6936` n `7`; unknown avg `3.7672` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.131`, n `490`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1175`, n `490`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0871`, n `486`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.082`, n `486`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0774`, n `486`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `486`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `490`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0699`, n `486`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0686`, n `490`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `486`, weak_sample_signal
