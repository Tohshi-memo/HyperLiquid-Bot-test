# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T05:37:28.578431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.043` n `12`; crypto_alt avg `0.0493` n `234`; crypto_major avg `0.1624` n `8`; equity avg `0.045` n `140`; fx avg `-0.0172` n `6`; index avg `-0.0018` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.1739` n `919`
- 1h: commodity avg `-0.05` n `12`; crypto_alt avg `0.2536` n `234`; crypto_major avg `0.4792` n `8`; equity avg `0.2263` n `140`; fx avg `-0.0241` n `6`; index avg `0.0372` n `26`; metal avg `0.1006` n `20`; unknown avg `-0.2793` n `917`
- 4h: commodity avg `-0.0469` n `12`; crypto_alt avg `1.8467` n `234`; crypto_major avg `1.6556` n `8`; equity avg `0.911` n `140`; fx avg `0.1124` n `6`; index avg `0.1503` n `26`; metal avg `0.1876` n `20`; unknown avg `9.8985` n `897`
- 24h: commodity avg `-0.3101` n `12`; crypto_alt avg `5.1086` n `234`; crypto_major avg `3.9632` n `8`; equity avg `2.341` n `140`; fx avg `0.1427` n `6`; index avg `0.3741` n `26`; metal avg `0.5893` n `20`; unknown avg `2.6848` n `753`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
