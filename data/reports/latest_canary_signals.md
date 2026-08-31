# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T23:22:26.945639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `12`; crypto_alt avg `0.0229` n `232`; crypto_major avg `0.0728` n `8`; equity avg `-0.0177` n `129`; fx avg `-0.0019` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0282` n `20`; unknown avg `1.0948` n `793`
- 1h: commodity avg `0.0304` n `12`; crypto_alt avg `0.0551` n `232`; crypto_major avg `-0.1846` n `8`; equity avg `-0.0782` n `129`; fx avg `0.0005` n `6`; index avg `-0.0062` n `26`; metal avg `-0.0362` n `20`; unknown avg `1.357` n `791`
- 4h: commodity avg `0.1307` n `12`; crypto_alt avg `0.0393` n `232`; crypto_major avg `-0.397` n `8`; equity avg `0.376` n `129`; fx avg `0.002` n `6`; index avg `0.058` n `26`; metal avg `0.0302` n `20`; unknown avg `2.3089` n `773`
- 24h: commodity avg `0.4588` n `12`; crypto_alt avg `0.55` n `231`; crypto_major avg `0.5446` n `8`; equity avg `0.747` n `129`; fx avg `-0.094` n `6`; index avg `0.0046` n `26`; metal avg `-0.3728` n `20`; unknown avg `1.3974` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
