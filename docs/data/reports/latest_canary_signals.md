# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T21:22:27.213427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `13`; crypto_alt avg `0.0363` n `238`; crypto_major avg `-0.0086` n `8`; equity avg `-0.0032` n `156`; fx avg `0.0104` n `6`; index avg `-0.0004` n `27`; metal avg `0.0037` n `20`; unknown avg `0.1976` n `1248`
- 1h: commodity avg `0.0238` n `13`; crypto_alt avg `0.0352` n `238`; crypto_major avg `-0.1412` n `8`; equity avg `0.0077` n `156`; fx avg `-0.0031` n `6`; index avg `-0.0017` n `27`; metal avg `-0.0038` n `20`; unknown avg `-0.0628` n `1212`
- 4h: commodity avg `0.0232` n `13`; crypto_alt avg `-0.4501` n `238`; crypto_major avg `-0.068` n `8`; equity avg `0.025` n `156`; fx avg `-0.0021` n `6`; index avg `-0.0022` n `27`; metal avg `-0.0123` n `20`; unknown avg `0.2749` n `1154`
- 24h: commodity avg `-0.0628` n `13`; crypto_alt avg `0.2425` n `238`; crypto_major avg `0.0346` n `8`; equity avg `0.2447` n `156`; fx avg `-0.0054` n `6`; index avg `-0.0236` n `27`; metal avg `0.0739` n `20`; unknown avg `1.7123` n `1077`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
