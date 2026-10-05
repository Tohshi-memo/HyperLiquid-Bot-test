# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T20:14:11.303952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0516` n `13`; crypto_alt avg `0.4004` n `235`; crypto_major avg `0.196` n `8`; equity avg `0.0774` n `144`; fx avg `-0.0088` n `6`; index avg `0.0203` n `26`; metal avg `-0.01` n `20`; unknown avg `35.869` n `1031`
- 1h: commodity avg `0.0413` n `13`; crypto_alt avg `0.407` n `235`; crypto_major avg `0.3914` n `8`; equity avg `0.1045` n `144`; fx avg `0.0009` n `6`; index avg `-0.0084` n `26`; metal avg `-0.0414` n `20`; unknown avg `22.9547` n `1031`
- 4h: commodity avg `-0.1323` n `13`; crypto_alt avg `0.8538` n `235`; crypto_major avg `0.6387` n `8`; equity avg `0.1603` n `144`; fx avg `0.015` n `6`; index avg `0.0555` n `26`; metal avg `0.0342` n `20`; unknown avg `4.1473` n `1031`
- 24h: commodity avg `-0.3966` n `13`; crypto_alt avg `0.4977` n `235`; crypto_major avg `0.5805` n `8`; equity avg `0.3804` n `144`; fx avg `-0.0844` n `6`; index avg `0.1314` n `26`; metal avg `0.1686` n `20`; unknown avg `2.819` n `814`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2002`, n `670`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.18`, n `670`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1709`, n `670`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1249`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `670`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1008`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `670`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `670`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0937`, n `670`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `670`, weak_sample_signal
