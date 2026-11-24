# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T13:07:30.323412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.2139` n `239`; crypto_major avg `-0.0686` n `8`; equity avg `-0.1639` n `166`; fx avg `0.026` n `6`; index avg `-0.0145` n `27`; metal avg `-0.1314` n `20`; unknown avg `-0.2309` n `1255`
- 1h: commodity avg `-0.0702` n `13`; crypto_alt avg `-0.4533` n `239`; crypto_major avg `-0.129` n `8`; equity avg `-0.142` n `166`; fx avg `0.0539` n `6`; index avg `-0.0212` n `27`; metal avg `0.077` n `20`; unknown avg `397.5996` n `1256`
- 4h: commodity avg `0.1788` n `13`; crypto_alt avg `-1.0181` n `239`; crypto_major avg `0.084` n `8`; equity avg `-0.598` n `166`; fx avg `0.1468` n `6`; index avg `-0.1272` n `27`; metal avg `0.1452` n `20`; unknown avg `176.7628` n `1214`
- 24h: commodity avg `-0.3497` n `13`; crypto_alt avg `-1.5926` n `239`; crypto_major avg `-1.208` n `8`; equity avg `1.4256` n `166`; fx avg `0.0266` n `6`; index avg `0.2903` n `27`; metal avg `-0.1777` n `20`; unknown avg `-0.2981` n `1136`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
