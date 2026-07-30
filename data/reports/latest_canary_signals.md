# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T18:22:36.240594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0226` n `12`; crypto_alt avg `-0.1011` n `230`; crypto_major avg `-0.0689` n `8`; equity avg `-0.0195` n `102`; fx avg `0.0127` n `6`; index avg `0.0328` n `25`; metal avg `0.0087` n `20`; unknown avg `0.0257` n `779`
- 1h: commodity avg `-0.0048` n `12`; crypto_alt avg `0.1153` n `230`; crypto_major avg `0.0444` n `8`; equity avg `-0.1151` n `102`; fx avg `-0.0969` n `6`; index avg `0.0249` n `25`; metal avg `0.0114` n `20`; unknown avg `0.0036` n `779`
- 4h: commodity avg `0.1329` n `12`; crypto_alt avg `-0.2682` n `230`; crypto_major avg `0.4512` n `8`; equity avg `-0.0943` n `102`; fx avg `0.0164` n `6`; index avg `0.0426` n `25`; metal avg `0.2698` n `20`; unknown avg `-0.0633` n `779`
- 24h: commodity avg `-0.0938` n `12`; crypto_alt avg `0.1279` n `230`; crypto_major avg `0.9373` n `8`; equity avg `3.8717` n `102`; fx avg `-0.3745` n `6`; index avg `0.3776` n `25`; metal avg `0.476` n `20`; unknown avg `-0.061` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
