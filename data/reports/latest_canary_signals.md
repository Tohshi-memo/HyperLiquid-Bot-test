# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T23:22:31.356905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `0.8137` n `234`; crypto_major avg `0.639` n `8`; equity avg `0.136` n `137`; fx avg `0.0026` n `6`; index avg `0.0193` n `27`; metal avg `0.0747` n `20`; unknown avg `0.4177` n `919`
- 1h: commodity avg `0.0191` n `12`; crypto_alt avg `0.9196` n `234`; crypto_major avg `0.6098` n `8`; equity avg `0.3167` n `137`; fx avg `0.0009` n `6`; index avg `0.0563` n `27`; metal avg `0.0826` n `20`; unknown avg `0.276` n `877`
- 4h: commodity avg `-0.0247` n `12`; crypto_alt avg `1.6117` n `234`; crypto_major avg `0.8093` n `8`; equity avg `1.6863` n `137`; fx avg `0.0284` n `6`; index avg `0.2765` n `27`; metal avg `0.2319` n `20`; unknown avg `0.6064` n `773`
- 24h: commodity avg `-0.5996` n `12`; crypto_alt avg `0.4012` n `234`; crypto_major avg `0.4533` n `8`; equity avg `1.3652` n `137`; fx avg `0.071` n `6`; index avg `0.1073` n `27`; metal avg `-0.2199` n `20`; unknown avg `-0.6909` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
