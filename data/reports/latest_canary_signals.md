# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T14:52:28.835932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0424` n `12`; crypto_alt avg `0.2456` n `228`; crypto_major avg `0.2838` n `8`; equity avg `-0.0029` n `86`; fx avg `-0.0028` n `6`; index avg `0.0167` n `23`; metal avg `0.105` n `20`; unknown avg `-0.0129` n `765`
- 1h: commodity avg `-0.02` n `12`; crypto_alt avg `0.6115` n `228`; crypto_major avg `0.8116` n `8`; equity avg `0.8841` n `86`; fx avg `-0.01` n `6`; index avg `0.1869` n `23`; metal avg `0.3305` n `20`; unknown avg `0.1033` n `765`
- 4h: commodity avg `-0.1112` n `12`; crypto_alt avg `0.9734` n `228`; crypto_major avg `1.1733` n `8`; equity avg `1.0429` n `86`; fx avg `-0.0081` n `6`; index avg `0.1184` n `23`; metal avg `0.3948` n `20`; unknown avg `0.1578` n `765`
- 24h: commodity avg `-0.0814` n `12`; crypto_alt avg `0.7787` n `228`; crypto_major avg `1.5639` n `8`; equity avg `-1.132` n `86`; fx avg `0.0395` n `6`; index avg `-0.3118` n `23`; metal avg `0.7391` n `20`; unknown avg `-0.0472` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3769`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2527`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
