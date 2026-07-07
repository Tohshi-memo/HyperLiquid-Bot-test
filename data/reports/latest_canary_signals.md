# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T07:56:24.482354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `12`; crypto_alt avg `0.0127` n `229`; crypto_major avg `-0.0047` n `8`; equity avg `-0.0652` n `91`; fx avg `-0.0387` n `6`; index avg `-0.0286` n `25`; metal avg `-0.0499` n `20`; unknown avg `-0.0816` n `763`
- 1h: commodity avg `0.0713` n `12`; crypto_alt avg `-0.2584` n `229`; crypto_major avg `-0.2808` n `8`; equity avg `-0.1024` n `91`; fx avg `-0.0627` n `6`; index avg `-0.0236` n `25`; metal avg `-0.0212` n `20`; unknown avg `-0.1569` n `763`
- 4h: commodity avg `0.2723` n `12`; crypto_alt avg `0.1256` n `229`; crypto_major avg `0.1359` n `8`; equity avg `0.328` n `91`; fx avg `-0.0231` n `6`; index avg `0.0568` n `25`; metal avg `-0.0053` n `20`; unknown avg `6.6882` n `745`
- 24h: commodity avg `0.6042` n `12`; crypto_alt avg `0.2117` n `229`; crypto_major avg `-0.5507` n `8`; equity avg `-1.3893` n `90`; fx avg `-0.0675` n `6`; index avg `-0.3699` n `25`; metal avg `-0.5621` n `20`; unknown avg `-0.4832` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
