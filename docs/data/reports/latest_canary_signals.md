# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T09:07:27.783570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0353` n `12`; crypto_alt avg `0.125` n `234`; crypto_major avg `0.1017` n `8`; equity avg `0.012` n `140`; fx avg `-0.0002` n `6`; index avg `0.0011` n `26`; metal avg `0.0128` n `20`; unknown avg `4.5174` n `941`
- 1h: commodity avg `-0.0244` n `12`; crypto_alt avg `-0.3694` n `234`; crypto_major avg `-0.2149` n `8`; equity avg `-0.0556` n `140`; fx avg `0.003` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0031` n `20`; unknown avg `6.1856` n `941`
- 4h: commodity avg `0.0013` n `12`; crypto_alt avg `-0.732` n `234`; crypto_major avg `-0.3338` n `8`; equity avg `-0.0668` n `140`; fx avg `0.0049` n `6`; index avg `-0.0116` n `26`; metal avg `0.0132` n `20`; unknown avg `2.5363` n `905`
- 24h: commodity avg `0.2368` n `12`; crypto_alt avg `-1.4609` n `234`; crypto_major avg `-2.2285` n `8`; equity avg `-0.2773` n `140`; fx avg `-0.065` n `6`; index avg `-0.0652` n `26`; metal avg `0.0251` n `20`; unknown avg `4.9708` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
