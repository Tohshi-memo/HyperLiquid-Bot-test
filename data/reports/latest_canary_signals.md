# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T02:37:29.020148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `-0.0589` n `239`; crypto_major avg `-0.0752` n `8`; equity avg `0.0134` n `161`; fx avg `0.006` n `6`; index avg `0.0145` n `27`; metal avg `-0.0656` n `20`; unknown avg `2.5369` n `1264`
- 1h: commodity avg `0.1426` n `13`; crypto_alt avg `0.2493` n `239`; crypto_major avg `0.3271` n `8`; equity avg `0.4908` n `161`; fx avg `-0.0288` n `6`; index avg `0.0688` n `27`; metal avg `-0.0617` n `20`; unknown avg `19.9498` n `1256`
- 4h: commodity avg `0.0114` n `13`; crypto_alt avg `-0.3113` n `239`; crypto_major avg `-0.2967` n `8`; equity avg `0.2624` n `161`; fx avg `-0.0528` n `6`; index avg `0.0585` n `27`; metal avg `-0.0288` n `20`; unknown avg `22.0248` n `1250`
- 24h: commodity avg `0.1699` n `13`; crypto_alt avg `-1.3088` n `239`; crypto_major avg `0.0442` n `8`; equity avg `1.9424` n `161`; fx avg `-0.1603` n `6`; index avg `0.201` n `27`; metal avg `-0.3829` n `20`; unknown avg `4.2231` n `1141`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
