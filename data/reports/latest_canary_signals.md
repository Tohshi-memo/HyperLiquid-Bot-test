# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T00:22:25.638260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0387` n `12`; crypto_alt avg `-0.0165` n `229`; crypto_major avg `0.0466` n `8`; equity avg `0.4196` n `91`; fx avg `-0.0058` n `6`; index avg `0.0465` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.08` n `763`
- 1h: commodity avg `0.0716` n `12`; crypto_alt avg `-0.2014` n `229`; crypto_major avg `-0.3293` n `8`; equity avg `0.4943` n `91`; fx avg `0.0459` n `6`; index avg `0.0502` n `25`; metal avg `-0.0634` n `20`; unknown avg `1.5525` n `763`
- 4h: commodity avg `0.1573` n `12`; crypto_alt avg `-0.6863` n `229`; crypto_major avg `-0.6112` n `8`; equity avg `0.0858` n `91`; fx avg `0.0504` n `6`; index avg `0.0042` n `25`; metal avg `-0.1689` n `20`; unknown avg `-0.0712` n `763`
- 24h: commodity avg `0.9507` n `12`; crypto_alt avg `-2.7753` n `229`; crypto_major avg `-1.817` n `8`; equity avg `-2.6075` n `91`; fx avg `-0.2052` n `6`; index avg `-0.4689` n `25`; metal avg `-0.6356` n `20`; unknown avg `-0.2694` n `729`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
