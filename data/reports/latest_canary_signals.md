# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T07:52:28.413176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2041` n `12`; crypto_alt avg `0.0691` n `228`; crypto_major avg `-0.1199` n `8`; equity avg `0.1563` n `74`; fx avg `-0.008` n `6`; index avg `0.0924` n `23`; metal avg `-0.0288` n `18`; unknown avg `0.0797` n `531`
- 1h: commodity avg `-0.3846` n `12`; crypto_alt avg `0.2252` n `228`; crypto_major avg `0.0954` n `8`; equity avg `0.1523` n `74`; fx avg `-0.0129` n `6`; index avg `0.0309` n `23`; metal avg `-0.2794` n `18`; unknown avg `0.1446` n `531`
- 4h: commodity avg `-0.485` n `12`; crypto_alt avg `-0.8659` n `228`; crypto_major avg `-1.1201` n `8`; equity avg `-0.8616` n `74`; fx avg `-0.0219` n `6`; index avg `-0.3635` n `23`; metal avg `-0.8104` n `18`; unknown avg `-0.0173` n `515`
- 24h: commodity avg `-2.0875` n `12`; crypto_alt avg `1.1048` n `228`; crypto_major avg `1.0264` n `8`; equity avg `2.3386` n `74`; fx avg `-0.0536` n `6`; index avg `1.3657` n `23`; metal avg `1.9037` n `18`; unknown avg `2.1254` n `514`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
