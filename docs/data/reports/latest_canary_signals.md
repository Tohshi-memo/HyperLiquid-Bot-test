# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T18:22:29.634806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1051` n `12`; crypto_alt avg `-0.1649` n `228`; crypto_major avg `-0.1706` n `8`; equity avg `-0.2693` n `74`; fx avg `-0.0005` n `6`; index avg `-0.1846` n `23`; metal avg `-0.118` n `18`; unknown avg `-0.0119` n `550`
- 1h: commodity avg `-0.3239` n `12`; crypto_alt avg `-0.5939` n `228`; crypto_major avg `-0.5157` n `8`; equity avg `0.1934` n `74`; fx avg `-0.0046` n `6`; index avg `0.0164` n `23`; metal avg `0.0943` n `18`; unknown avg `-0.3746` n `549`
- 4h: commodity avg `0.1532` n `12`; crypto_alt avg `-1.2677` n `228`; crypto_major avg `-1.3379` n `8`; equity avg `-1.3501` n `74`; fx avg `-0.0041` n `6`; index avg `-1.138` n `23`; metal avg `-0.7526` n `18`; unknown avg `0.0109` n `548`
- 24h: commodity avg `1.3379` n `12`; crypto_alt avg `-1.3391` n `228`; crypto_major avg `-2.1005` n `8`; equity avg `-0.4825` n `74`; fx avg `-0.0477` n `6`; index avg `-0.2513` n `23`; metal avg `-1.6335` n `18`; unknown avg `-0.1896` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
