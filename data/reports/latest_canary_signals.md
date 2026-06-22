# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T23:07:33.766793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0284` n `12`; crypto_alt avg `0.0066` n `228`; crypto_major avg `0.0205` n `8`; equity avg `-0.0048` n `86`; fx avg `0.0305` n `6`; index avg `-0.0057` n `23`; metal avg `0.0298` n `20`; unknown avg `-0.0301` n `716`
- 1h: commodity avg `0.0088` n `12`; crypto_alt avg `-0.8399` n `228`; crypto_major avg `-0.4984` n `8`; equity avg `-0.2433` n `86`; fx avg `0.0375` n `6`; index avg `-0.017` n `23`; metal avg `-0.0259` n `20`; unknown avg `-0.2524` n `716`
- 4h: commodity avg `-0.0113` n `12`; crypto_alt avg `-1.0139` n `228`; crypto_major avg `-0.7161` n `8`; equity avg `-0.1879` n `86`; fx avg `0.0248` n `6`; index avg `0.0178` n `23`; metal avg `-0.0215` n `20`; unknown avg `-0.3655` n `708`
- 24h: commodity avg `-0.8492` n `12`; crypto_alt avg `-0.5806` n `228`; crypto_major avg `-0.0964` n `8`; equity avg `-0.4595` n `85`; fx avg `0.1094` n `6`; index avg `0.1912` n `23`; metal avg `0.2512` n `18`; unknown avg `0.3465` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
