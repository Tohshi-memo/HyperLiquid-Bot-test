# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T17:37:28.317492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0379` n `12`; crypto_alt avg `0.1442` n `230`; crypto_major avg `0.1539` n `8`; equity avg `-0.0` n `96`; fx avg `0.0` n `6`; index avg `-0.0049` n `25`; metal avg `0.0004` n `20`; unknown avg `0.0263` n `770`
- 1h: commodity avg `0.0624` n `12`; crypto_alt avg `0.217` n `230`; crypto_major avg `0.1829` n `8`; equity avg `0.0327` n `96`; fx avg `-0.0111` n `6`; index avg `-0.0037` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.0468` n `770`
- 4h: commodity avg `0.048` n `12`; crypto_alt avg `0.4734` n `230`; crypto_major avg `0.5232` n `8`; equity avg `-0.032` n `96`; fx avg `-0.0546` n `6`; index avg `-0.0228` n `25`; metal avg `-0.0445` n `20`; unknown avg `0.0502` n `770`
- 24h: commodity avg `0.2917` n `12`; crypto_alt avg `-0.9019` n `230`; crypto_major avg `-0.0552` n `8`; equity avg `-1.5907` n `96`; fx avg `-0.119` n `6`; index avg `-0.1435` n `25`; metal avg `-0.0272` n `20`; unknown avg `-0.1151` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
