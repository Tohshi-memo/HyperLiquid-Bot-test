# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T05:37:16.493355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0961` n `12`; crypto_alt avg `0.0555` n `228`; crypto_major avg `-0.0528` n `8`; equity avg `0.0027` n `67`; fx avg `0.0033` n `6`; index avg `-0.0221` n `23`; metal avg `0.0184` n `18`; unknown avg `-0.3302` n `397`
- 1h: commodity avg `-0.0799` n `12`; crypto_alt avg `0.6772` n `228`; crypto_major avg `0.4447` n `8`; equity avg `0.1624` n `67`; fx avg `0.0078` n `6`; index avg `-0.0558` n `23`; metal avg `-0.0954` n `18`; unknown avg `-0.886` n `397`
- 4h: commodity avg `-0.6119` n `12`; crypto_alt avg `0.845` n `228`; crypto_major avg `0.342` n `8`; equity avg `0.4936` n `67`; fx avg `-0.0012` n `6`; index avg `0.1001` n `23`; metal avg `-0.2096` n `18`; unknown avg `-0.4651` n `396`
- 24h: commodity avg `-0.0174` n `12`; crypto_alt avg `0.3725` n `228`; crypto_major avg `0.6058` n `8`; equity avg `0.6136` n `67`; fx avg `-0.0478` n `6`; index avg `-0.1494` n `23`; metal avg `0.4551` n `18`; unknown avg `-0.04` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
