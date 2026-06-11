# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T16:52:35.604293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.191` n `12`; crypto_alt avg `-0.474` n `228`; crypto_major avg `-0.3802` n `8`; equity avg `-0.4996` n `74`; fx avg `-0.0005` n `6`; index avg `-0.1181` n `23`; metal avg `-0.203` n `18`; unknown avg `-0.4183` n `556`
- 1h: commodity avg `-0.1196` n `12`; crypto_alt avg `-0.1258` n `228`; crypto_major avg `-0.1493` n `8`; equity avg `-0.1323` n `74`; fx avg `-0.0163` n `6`; index avg `0.0082` n `23`; metal avg `-0.3169` n `18`; unknown avg `-0.632` n `556`
- 4h: commodity avg `-0.1792` n `12`; crypto_alt avg `0.0423` n `228`; crypto_major avg `-0.301` n `8`; equity avg `0.0968` n `74`; fx avg `-0.108` n `6`; index avg `0.1665` n `23`; metal avg `0.2642` n `18`; unknown avg `-0.3221` n `556`
- 24h: commodity avg `-0.7021` n `12`; crypto_alt avg `0.8399` n `228`; crypto_major avg `0.5341` n `8`; equity avg `-0.078` n `74`; fx avg `-0.0735` n `6`; index avg `0.1898` n `23`; metal avg `-0.7189` n `18`; unknown avg `1.7755` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
