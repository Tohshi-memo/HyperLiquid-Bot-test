# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T14:22:36.053257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.124` n `12`; crypto_alt avg `-0.2652` n `228`; crypto_major avg `-0.3621` n `8`; equity avg `-0.7006` n `74`; fx avg `0.0005` n `6`; index avg `-0.3341` n `23`; metal avg `-0.2149` n `18`; unknown avg `0.0173` n `556`
- 1h: commodity avg `-0.5307` n `12`; crypto_alt avg `-0.0062` n `228`; crypto_major avg `-0.1099` n `8`; equity avg `0.1229` n `74`; fx avg `-0.014` n `6`; index avg `0.0996` n `23`; metal avg `0.1393` n `18`; unknown avg `0.1034` n `556`
- 4h: commodity avg `0.1756` n `12`; crypto_alt avg `-0.0247` n `228`; crypto_major avg `-0.0403` n `8`; equity avg `-0.4136` n `74`; fx avg `-0.0129` n `6`; index avg `-0.0868` n `23`; metal avg `0.078` n `18`; unknown avg `-1.3372` n `556`
- 24h: commodity avg `-0.428` n `12`; crypto_alt avg `0.3251` n `228`; crypto_major avg `-0.0063` n `8`; equity avg `-1.3706` n `74`; fx avg `-0.0044` n `6`; index avg `-0.896` n `23`; metal avg `-1.2807` n `18`; unknown avg `2.3935` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
