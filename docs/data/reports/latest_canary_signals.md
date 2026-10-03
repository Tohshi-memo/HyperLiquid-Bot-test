# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T03:37:37.038170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `13`; crypto_alt avg `-0.0301` n `235`; crypto_major avg `0.0242` n `8`; equity avg `0.0024` n `143`; fx avg `0.001` n `6`; index avg `-0.0004` n `26`; metal avg `0.0032` n `20`; unknown avg `0.0143` n `984`
- 1h: commodity avg `-0.0017` n `13`; crypto_alt avg `0.1734` n `235`; crypto_major avg `-0.1133` n `8`; equity avg `-0.0473` n `143`; fx avg `-0.0021` n `6`; index avg `-0.0056` n `26`; metal avg `-0.0095` n `20`; unknown avg `-0.2631` n `982`
- 4h: commodity avg `-0.1921` n `13`; crypto_alt avg `0.5509` n `235`; crypto_major avg `0.0282` n `8`; equity avg `-0.0085` n `143`; fx avg `0.012` n `6`; index avg `0.0331` n `26`; metal avg `-0.0122` n `20`; unknown avg `-0.2008` n `976`
- 24h: commodity avg `0.0614` n `13`; crypto_alt avg `-0.268` n `235`; crypto_major avg `-0.7919` n `8`; equity avg `0.6161` n `142`; fx avg `-0.121` n `6`; index avg `0.2646` n `26`; metal avg `-0.2377` n `20`; unknown avg `-0.7892` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
