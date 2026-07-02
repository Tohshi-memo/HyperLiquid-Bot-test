# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T06:52:32.059970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0598` n `12`; crypto_alt avg `-0.1983` n `228`; crypto_major avg `-0.4495` n `8`; equity avg `-0.3447` n `88`; fx avg `-0.0612` n `6`; index avg `-0.0563` n `25`; metal avg `-0.0781` n `20`; unknown avg `-0.1259` n `763`
- 1h: commodity avg `-0.1118` n `12`; crypto_alt avg `-0.2683` n `228`; crypto_major avg `-0.3273` n `8`; equity avg `-0.8074` n `88`; fx avg `-0.071` n `6`; index avg `-0.1401` n `25`; metal avg `0.0517` n `20`; unknown avg `-0.2457` n `741`
- 4h: commodity avg `-0.0812` n `12`; crypto_alt avg `-0.1688` n `228`; crypto_major avg `-0.1881` n `8`; equity avg `-1.4243` n `88`; fx avg `-0.0596` n `6`; index avg `-0.3146` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.3534` n `739`
- 24h: commodity avg `-0.5755` n `12`; crypto_alt avg `1.9071` n `228`; crypto_major avg `1.3556` n `8`; equity avg `-2.3977` n `88`; fx avg `-0.0794` n `6`; index avg `-0.5704` n `25`; metal avg `1.1866` n `20`; unknown avg `24.9039` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
