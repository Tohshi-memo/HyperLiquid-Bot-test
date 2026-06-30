# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T07:37:33.655762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `12`; crypto_alt avg `-0.0544` n `228`; crypto_major avg `0.057` n `8`; equity avg `0.0559` n `88`; fx avg `0.0072` n `6`; index avg `0.0104` n `23`; metal avg `0.0136` n `20`; unknown avg `0.8307` n `765`
- 1h: commodity avg `0.0934` n `12`; crypto_alt avg `-0.3142` n `228`; crypto_major avg `-0.1192` n `8`; equity avg `0.1115` n `88`; fx avg `0.0187` n `6`; index avg `0.0126` n `23`; metal avg `-0.0197` n `20`; unknown avg `0.1059` n `765`
- 4h: commodity avg `0.0201` n `12`; crypto_alt avg `-0.2743` n `228`; crypto_major avg `-0.2924` n `8`; equity avg `0.0588` n `88`; fx avg `0.0514` n `6`; index avg `0.0254` n `23`; metal avg `0.7034` n `20`; unknown avg `6.9913` n `737`
- 24h: commodity avg `-0.0317` n `12`; crypto_alt avg `-0.6101` n `228`; crypto_major avg `0.5854` n `8`; equity avg `1.7659` n `88`; fx avg `0.1573` n `6`; index avg `0.1823` n `23`; metal avg `-0.0281` n `20`; unknown avg `9.3768` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
