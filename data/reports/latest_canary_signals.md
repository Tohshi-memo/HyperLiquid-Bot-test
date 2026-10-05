# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T00:52:31.201778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0264` n `13`; crypto_alt avg `0.2213` n `235`; crypto_major avg `0.3515` n `8`; equity avg `0.0647` n `144`; fx avg `0.0063` n `6`; index avg `0.0146` n `26`; metal avg `0.0155` n `20`; unknown avg `0.8284` n `1076`
- 1h: commodity avg `0.017` n `13`; crypto_alt avg `0.2079` n `235`; crypto_major avg `0.0763` n `8`; equity avg `0.1675` n `144`; fx avg `0.0083` n `6`; index avg `0.0345` n `26`; metal avg `0.1299` n `20`; unknown avg `0.2661` n `1060`
- 4h: commodity avg `-0.2356` n `13`; crypto_alt avg `0.672` n `235`; crypto_major avg `0.4845` n `8`; equity avg `0.3755` n `144`; fx avg `0.002` n `6`; index avg `0.0368` n `26`; metal avg `0.1802` n `20`; unknown avg `0.7013` n `996`
- 24h: commodity avg `-0.2206` n `13`; crypto_alt avg `1.3065` n `235`; crypto_major avg `1.6628` n `8`; equity avg `0.5535` n `144`; fx avg `0.0185` n `6`; index avg `0.0273` n `26`; metal avg `0.1937` n `20`; unknown avg `0.6104` n `954`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1809`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
