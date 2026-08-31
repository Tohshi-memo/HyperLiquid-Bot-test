# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T22:22:25.575917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `-0.248` n `232`; crypto_major avg `-0.2356` n `8`; equity avg `-0.0152` n `129`; fx avg `-0.0047` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0188` n `20`; unknown avg `0.2192` n `793`
- 1h: commodity avg `-0.014` n `12`; crypto_alt avg `0.1018` n `232`; crypto_major avg `0.0153` n `8`; equity avg `0.0621` n `129`; fx avg `0.0036` n `6`; index avg `-0.019` n `26`; metal avg `0.0104` n `20`; unknown avg `0.4681` n `791`
- 4h: commodity avg `0.0684` n `12`; crypto_alt avg `-0.0913` n `232`; crypto_major avg `-0.1272` n `8`; equity avg `0.3994` n `129`; fx avg `-0.0011` n `6`; index avg `0.0393` n `26`; metal avg `0.0837` n `20`; unknown avg `0.7197` n `773`
- 24h: commodity avg `0.3239` n `12`; crypto_alt avg `-0.0264` n `231`; crypto_major avg `0.2887` n `8`; equity avg `0.2824` n `129`; fx avg `-0.0834` n `6`; index avg `-0.0798` n `26`; metal avg `-0.3091` n `20`; unknown avg `-0.1098` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
