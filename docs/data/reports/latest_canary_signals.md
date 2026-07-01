# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T20:37:37.144953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `0.0581` n `228`; crypto_major avg `-0.053` n `8`; equity avg `0.011` n `88`; fx avg `0.0017` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0175` n `20`; unknown avg `-0.1584` n `763`
- 1h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.2361` n `228`; crypto_major avg `-0.5745` n `8`; equity avg `-0.6291` n `88`; fx avg `0.0074` n `6`; index avg `-0.1181` n `25`; metal avg `-0.2047` n `20`; unknown avg `1.3533` n `763`
- 4h: commodity avg `-0.1005` n `12`; crypto_alt avg `-1.0224` n `228`; crypto_major avg `-0.8402` n `8`; equity avg `-1.222` n `88`; fx avg `0.0094` n `6`; index avg `-0.2016` n `25`; metal avg `-0.4381` n `20`; unknown avg `0.114` n `761`
- 24h: commodity avg `-0.6146` n `12`; crypto_alt avg `1.4566` n `228`; crypto_major avg `1.0259` n `8`; equity avg `-1.7434` n `88`; fx avg `-0.0014` n `6`; index avg `-0.543` n `25`; metal avg `0.1469` n `20`; unknown avg `0.199` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
