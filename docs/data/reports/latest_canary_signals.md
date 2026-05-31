# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T16:07:23.260258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0561` n `12`; crypto_alt avg `0.0103` n `228`; crypto_major avg `0.0711` n `8`; equity avg `0.0557` n `69`; fx avg `-0.0016` n `6`; index avg `0.0449` n `23`; metal avg `-0.0088` n `18`; unknown avg `0.0007` n `421`
- 1h: commodity avg `0.126` n `12`; crypto_alt avg `0.2022` n `228`; crypto_major avg `0.0973` n `8`; equity avg `0.1204` n `69`; fx avg `-0.0144` n `6`; index avg `0.1618` n `23`; metal avg `-0.0496` n `18`; unknown avg `-0.168` n `421`
- 4h: commodity avg `0.2005` n `12`; crypto_alt avg `-0.792` n `228`; crypto_major avg `-0.2166` n `8`; equity avg `0.1646` n `69`; fx avg `-0.0196` n `6`; index avg `0.1407` n `23`; metal avg `-0.0681` n `18`; unknown avg `-0.4744` n `421`
- 24h: commodity avg `1.1777` n `12`; crypto_alt avg `-0.9932` n `228`; crypto_major avg `0.1797` n `8`; equity avg `0.9296` n `69`; fx avg `-0.027` n `6`; index avg `0.0293` n `23`; metal avg `-0.1433` n `18`; unknown avg `0.2341` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
