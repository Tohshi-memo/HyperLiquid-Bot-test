# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T13:37:28.689602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.1138` n `229`; crypto_major avg `-0.1154` n `8`; equity avg `-0.1729` n `91`; fx avg `0.0128` n `6`; index avg `-0.024` n `25`; metal avg `0.1297` n `20`; unknown avg `-0.0083` n `763`
- 1h: commodity avg `0.2746` n `12`; crypto_alt avg `-0.5569` n `229`; crypto_major avg `-0.5936` n `8`; equity avg `-0.5551` n `91`; fx avg `0.0296` n `6`; index avg `-0.0778` n `25`; metal avg `0.0457` n `20`; unknown avg `-0.0632` n `763`
- 4h: commodity avg `-0.0549` n `12`; crypto_alt avg `-0.0683` n `229`; crypto_major avg `-0.1739` n `8`; equity avg `-0.4479` n `91`; fx avg `-0.056` n `6`; index avg `-0.0488` n `25`; metal avg `0.3643` n `20`; unknown avg `-0.0952` n `761`
- 24h: commodity avg `0.3911` n `12`; crypto_alt avg `1.474` n `229`; crypto_major avg `1.4314` n `8`; equity avg `-1.3576` n `90`; fx avg `-0.1717` n `6`; index avg `-0.3797` n `25`; metal avg `0.2151` n `20`; unknown avg `0.3274` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
