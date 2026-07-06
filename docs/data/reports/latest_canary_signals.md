# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T09:37:26.063086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.1216` n `229`; crypto_major avg `-0.2186` n `8`; equity avg `-0.0151` n `88`; fx avg `-0.0013` n `6`; index avg `0.0054` n `25`; metal avg `-0.1139` n `20`; unknown avg `0.0131` n `765`
- 1h: commodity avg `0.0551` n `12`; crypto_alt avg `-0.136` n `229`; crypto_major avg `-0.3066` n `8`; equity avg `0.0319` n `88`; fx avg `-0.0097` n `6`; index avg `0.0122` n `25`; metal avg `-0.0802` n `20`; unknown avg `-0.069` n `765`
- 4h: commodity avg `0.0078` n `12`; crypto_alt avg `-0.3581` n `229`; crypto_major avg `-0.6244` n `8`; equity avg `0.1135` n `88`; fx avg `0.0383` n `6`; index avg `0.0967` n `25`; metal avg `-0.0597` n `20`; unknown avg `-0.027` n `731`
- 24h: commodity avg `-0.1539` n `12`; crypto_alt avg `-0.4391` n `229`; crypto_major avg `0.3772` n `8`; equity avg `-0.5964` n `88`; fx avg `0.0823` n `6`; index avg `0.0024` n `25`; metal avg `-0.2993` n `20`; unknown avg `1.0558` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
