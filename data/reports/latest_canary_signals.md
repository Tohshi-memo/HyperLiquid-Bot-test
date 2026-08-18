# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T03:37:28.249615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `12`; crypto_alt avg `-0.0427` n `230`; crypto_major avg `-0.0074` n `8`; equity avg `0.0865` n `114`; fx avg `0.016` n `6`; index avg `0.0009` n `25`; metal avg `0.0077` n `20`; unknown avg `0.0741` n `793`
- 1h: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.5135` n `230`; crypto_major avg `-0.0672` n `8`; equity avg `-0.3307` n `114`; fx avg `0.0003` n `6`; index avg `-0.0717` n `25`; metal avg `-0.0129` n `20`; unknown avg `-0.0241` n `793`
- 4h: commodity avg `0.0111` n `12`; crypto_alt avg `-1.1767` n `230`; crypto_major avg `-0.654` n `8`; equity avg `-1.7579` n `114`; fx avg `-0.0444` n `6`; index avg `-0.3047` n `25`; metal avg `-0.2277` n `20`; unknown avg `0.624` n `793`
- 24h: commodity avg `0.5538` n `12`; crypto_alt avg `-1.5019` n `230`; crypto_major avg `-0.079` n `8`; equity avg `-1.227` n `114`; fx avg `-0.0255` n `6`; index avg `-0.2967` n `25`; metal avg `-0.1894` n `20`; unknown avg `0.0058` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
