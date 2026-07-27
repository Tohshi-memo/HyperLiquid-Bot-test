# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T22:37:32.609550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.1879` n `230`; crypto_major avg `-0.2025` n `8`; equity avg `-0.0726` n `102`; fx avg `0.0067` n `6`; index avg `0.0004` n `25`; metal avg `-0.0063` n `20`; unknown avg `1.8329` n `774`
- 1h: commodity avg `-0.0482` n `12`; crypto_alt avg `-0.4397` n `230`; crypto_major avg `-0.5029` n `8`; equity avg `-0.348` n `102`; fx avg `0.0049` n `6`; index avg `-0.0336` n `25`; metal avg `-0.032` n `20`; unknown avg `1.7092` n `774`
- 4h: commodity avg `-0.2031` n `12`; crypto_alt avg `-0.2031` n `230`; crypto_major avg `-0.3445` n `8`; equity avg `0.7134` n `102`; fx avg `-0.0157` n `6`; index avg `0.1106` n `25`; metal avg `0.0356` n `20`; unknown avg `1470.5961` n `774`
- 24h: commodity avg `-0.6132` n `12`; crypto_alt avg `-2.3065` n `230`; crypto_major avg `-1.9437` n `8`; equity avg `-1.7287` n `102`; fx avg `-0.0386` n `6`; index avg `-0.4853` n `25`; metal avg `-0.0515` n `20`; unknown avg `1503.2223` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1923`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
