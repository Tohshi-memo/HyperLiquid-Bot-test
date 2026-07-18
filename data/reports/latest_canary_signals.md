# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T18:52:28.893890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1296` n `12`; crypto_alt avg `-0.0707` n `230`; crypto_major avg `0.0474` n `8`; equity avg `-0.0128` n `96`; fx avg `0.0127` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.1446` n `770`
- 1h: commodity avg `0.2337` n `12`; crypto_alt avg `-0.2008` n `230`; crypto_major avg `0.0038` n `8`; equity avg `-0.0344` n `96`; fx avg `-0.0262` n `6`; index avg `-0.0258` n `25`; metal avg `-0.0246` n `20`; unknown avg `-0.072` n `770`
- 4h: commodity avg `0.3375` n `12`; crypto_alt avg `0.1214` n `230`; crypto_major avg `0.3134` n `8`; equity avg `-0.0658` n `96`; fx avg `-0.0724` n `6`; index avg `-0.035` n `25`; metal avg `-0.0414` n `20`; unknown avg `-0.0996` n `770`
- 24h: commodity avg `0.5584` n `12`; crypto_alt avg `-1.0212` n `230`; crypto_major avg `-0.032` n `8`; equity avg `-0.8243` n `96`; fx avg `-0.1356` n `6`; index avg `-0.0722` n `25`; metal avg `0.001` n `20`; unknown avg `-0.1146` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
