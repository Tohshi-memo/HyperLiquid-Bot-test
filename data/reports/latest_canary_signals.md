# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T17:07:30.321281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `0.1582` n `234`; crypto_major avg `0.0213` n `8`; equity avg `0.1156` n `140`; fx avg `0.0073` n `6`; index avg `0.0009` n `26`; metal avg `0.0267` n `20`; unknown avg `0.6386` n `940`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `0.4649` n `234`; crypto_major avg `0.0903` n `8`; equity avg `0.1885` n `140`; fx avg `-0.0156` n `6`; index avg `0.0293` n `26`; metal avg `0.1273` n `20`; unknown avg `-0.1861` n `900`
- 4h: commodity avg `0.5269` n `12`; crypto_alt avg `0.0927` n `234`; crypto_major avg `-0.0173` n `8`; equity avg `0.8818` n `140`; fx avg `-0.0553` n `6`; index avg `0.106` n `26`; metal avg `-0.0258` n `20`; unknown avg `0.8469` n `858`
- 24h: commodity avg `0.3052` n `12`; crypto_alt avg `1.609` n `234`; crypto_major avg `1.0541` n `8`; equity avg `0.8368` n `140`; fx avg `-0.2829` n `6`; index avg `0.1207` n `26`; metal avg `0.0949` n `20`; unknown avg `0.0993` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
