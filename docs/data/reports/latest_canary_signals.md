# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T14:19:04.263357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `-0.2385` n `230`; crypto_major avg `-0.3823` n `8`; equity avg `-0.3109` n `98`; fx avg `0.0115` n `6`; index avg `-0.012` n `25`; metal avg `-0.0742` n `20`; unknown avg `0.0815` n `773`
- 1h: commodity avg `0.1367` n `12`; crypto_alt avg `0.3258` n `230`; crypto_major avg `0.4254` n `8`; equity avg `0.8529` n `98`; fx avg `-0.0059` n `6`; index avg `0.1432` n `25`; metal avg `0.1563` n `20`; unknown avg `10.5763` n `773`
- 4h: commodity avg `0.111` n `12`; crypto_alt avg `0.2469` n `230`; crypto_major avg `0.0623` n `8`; equity avg `0.4288` n `98`; fx avg `-0.0086` n `6`; index avg `0.0691` n `25`; metal avg `0.1602` n `20`; unknown avg `11.2642` n `773`
- 24h: commodity avg `0.5249` n `12`; crypto_alt avg `-0.2678` n `230`; crypto_major avg `-1.0988` n `8`; equity avg `0.6139` n `98`; fx avg `-0.0195` n `6`; index avg `0.0378` n `25`; metal avg `0.5852` n `20`; unknown avg `0.9124` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.103`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0679`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0634`, n `666`, weak_sample_signal
