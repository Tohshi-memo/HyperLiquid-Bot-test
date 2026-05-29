# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T14:52:21.391775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4015` n `12`; crypto_alt avg `0.7822` n `228`; crypto_major avg `0.4844` n `8`; equity avg `0.1668` n `69`; fx avg `0.0488` n `6`; index avg `0.0794` n `23`; metal avg `0.5958` n `18`; unknown avg `0.1119` n `418`
- 1h: commodity avg `-0.1146` n `12`; crypto_alt avg `0.2977` n `228`; crypto_major avg `0.1533` n `8`; equity avg `-0.3365` n `69`; fx avg `0.0298` n `6`; index avg `-0.2263` n `23`; metal avg `0.1292` n `18`; unknown avg `-0.1913` n `417`
- 4h: commodity avg `0.0454` n `12`; crypto_alt avg `-0.6212` n `228`; crypto_major avg `-0.4775` n `8`; equity avg `-0.4496` n `69`; fx avg `0.0553` n `6`; index avg `-0.2294` n `23`; metal avg `0.0574` n `18`; unknown avg `1.1824` n `417`
- 24h: commodity avg `-0.2029` n `12`; crypto_alt avg `1.2517` n `228`; crypto_major avg `1.5999` n `8`; equity avg `1.6922` n `69`; fx avg `0.1475` n `6`; index avg `0.624` n `23`; metal avg `1.173` n `18`; unknown avg `1.7854` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
