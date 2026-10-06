# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T09:07:30.012132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `0.0869` n `235`; crypto_major avg `0.0788` n `8`; equity avg `0.067` n `149`; fx avg `0.0045` n `6`; index avg `0.0012` n `26`; metal avg `0.0062` n `20`; unknown avg `-0.1022` n `1072`
- 1h: commodity avg `-0.1286` n `13`; crypto_alt avg `0.0247` n `235`; crypto_major avg `0.1177` n `8`; equity avg `-0.0027` n `149`; fx avg `0.0168` n `6`; index avg `0.006` n `26`; metal avg `0.0362` n `20`; unknown avg `0.7646` n `1072`
- 4h: commodity avg `-0.4045` n `13`; crypto_alt avg `0.3421` n `235`; crypto_major avg `0.1085` n `8`; equity avg `0.1858` n `149`; fx avg `0.0245` n `6`; index avg `0.0649` n `26`; metal avg `0.1225` n `20`; unknown avg `-0.2065` n `976`
- 24h: commodity avg `-0.6597` n `13`; crypto_alt avg `-0.8692` n `235`; crypto_major avg `-0.54` n `8`; equity avg `0.4019` n `149`; fx avg `0.033` n `6`; index avg `0.2033` n `26`; metal avg `-0.195` n `20`; unknown avg `-0.116` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
