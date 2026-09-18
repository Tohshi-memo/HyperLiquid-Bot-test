# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T09:52:26.603542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0528` n `12`; crypto_alt avg `0.1684` n `234`; crypto_major avg `0.1508` n `8`; equity avg `-0.0327` n `140`; fx avg `0.0099` n `6`; index avg `-0.0149` n `26`; metal avg `-0.058` n `20`; unknown avg `0.2967` n `927`
- 1h: commodity avg `0.086` n `12`; crypto_alt avg `0.3025` n `234`; crypto_major avg `0.3354` n `8`; equity avg `-0.2605` n `140`; fx avg `0.0433` n `6`; index avg `-0.0546` n `26`; metal avg `-0.0955` n `20`; unknown avg `0.3628` n `925`
- 4h: commodity avg `-0.0346` n `12`; crypto_alt avg `1.2896` n `234`; crypto_major avg `0.9713` n `8`; equity avg `0.1537` n `140`; fx avg `0.1458` n `6`; index avg `0.0111` n `26`; metal avg `0.1055` n `20`; unknown avg `0.1916` n `863`
- 24h: commodity avg `-0.17` n `12`; crypto_alt avg `5.7147` n `234`; crypto_major avg `4.315` n `8`; equity avg `1.6839` n `140`; fx avg `0.2196` n `6`; index avg `0.2334` n `26`; metal avg `0.664` n `20`; unknown avg `2.5746` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
