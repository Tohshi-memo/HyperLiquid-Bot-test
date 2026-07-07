# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T08:52:29.166871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0618` n `12`; crypto_alt avg `-0.054` n `229`; crypto_major avg `-0.0002` n `8`; equity avg `-0.0165` n `91`; fx avg `-0.0117` n `6`; index avg `-0.0195` n `25`; metal avg `-0.0368` n `20`; unknown avg `-0.0054` n `763`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `-0.1477` n `229`; crypto_major avg `-0.119` n `8`; equity avg `-0.0075` n `91`; fx avg `0.0029` n `6`; index avg `0.0092` n `25`; metal avg `0.06` n `20`; unknown avg `2.7658` n `763`
- 4h: commodity avg `0.3038` n `12`; crypto_alt avg `0.141` n `229`; crypto_major avg `0.2938` n `8`; equity avg `0.5717` n `91`; fx avg `-0.0176` n `6`; index avg `0.0987` n `25`; metal avg `0.0558` n `20`; unknown avg `3.966` n `745`
- 24h: commodity avg `0.4448` n `12`; crypto_alt avg `0.4621` n `229`; crypto_major avg `-0.2916` n `8`; equity avg `-1.4327` n `90`; fx avg `-0.0683` n `6`; index avg `-0.3548` n `25`; metal avg `-0.3405` n `20`; unknown avg `-0.4704` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
