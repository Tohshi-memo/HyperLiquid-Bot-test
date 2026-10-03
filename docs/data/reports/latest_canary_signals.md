# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T04:07:27.870120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0092` n `13`; crypto_alt avg `-0.1882` n `235`; crypto_major avg `-0.0065` n `8`; equity avg `-0.0203` n `143`; fx avg `0.0012` n `6`; index avg `-0.001` n `26`; metal avg `-0.0053` n `20`; unknown avg `-0.1399` n `976`
- 1h: commodity avg `-0.0283` n `13`; crypto_alt avg `0.2302` n `235`; crypto_major avg `0.1916` n `8`; equity avg `-0.0287` n `143`; fx avg `0.001` n `6`; index avg `-0.0008` n `26`; metal avg `0.003` n `20`; unknown avg `-0.2071` n `976`
- 4h: commodity avg `-0.245` n `13`; crypto_alt avg `0.3618` n `235`; crypto_major avg `0.1588` n `8`; equity avg `-0.0527` n `143`; fx avg `0.0206` n `6`; index avg `0.0256` n `26`; metal avg `-0.0111` n `20`; unknown avg `-0.2364` n `976`
- 24h: commodity avg `0.0802` n `13`; crypto_alt avg `-0.4618` n `235`; crypto_major avg `-1.0221` n `8`; equity avg `0.5758` n `142`; fx avg `-0.1187` n `6`; index avg `0.2552` n `26`; metal avg `-0.306` n `20`; unknown avg `-0.9282` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
