# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T02:22:32.787035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0351` n `12`; crypto_alt avg `0.082` n `228`; crypto_major avg `0.3214` n `8`; equity avg `0.0501` n `74`; fx avg `-0.0078` n `6`; index avg `-0.0689` n `23`; metal avg `0.0028` n `18`; unknown avg `-0.0533` n `557`
- 1h: commodity avg `0.0016` n `12`; crypto_alt avg `0.4185` n `228`; crypto_major avg `0.3891` n `8`; equity avg `0.0893` n `74`; fx avg `0.0331` n `6`; index avg `-0.0102` n `23`; metal avg `0.3544` n `18`; unknown avg `0.3753` n `556`
- 4h: commodity avg `0.2603` n `12`; crypto_alt avg `0.0455` n `228`; crypto_major avg `-0.0131` n `8`; equity avg `0.2523` n `74`; fx avg `0.0213` n `6`; index avg `-0.1527` n `23`; metal avg `0.0762` n `18`; unknown avg `-0.2303` n `556`
- 24h: commodity avg `-2.4384` n `12`; crypto_alt avg `3.1894` n `228`; crypto_major avg `3.3854` n `8`; equity avg `4.4559` n `74`; fx avg `-0.0329` n `6`; index avg `2.2509` n `23`; metal avg `3.0784` n `18`; unknown avg `2.5496` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
