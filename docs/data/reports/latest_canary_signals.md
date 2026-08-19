# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T13:37:26.677245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `12`; crypto_alt avg `-0.0523` n `230`; crypto_major avg `-0.2148` n `8`; equity avg `-1.1973` n `121`; fx avg `0.0268` n `6`; index avg `-0.1101` n `25`; metal avg `-0.0155` n `20`; unknown avg `0.0945` n `792`
- 1h: commodity avg `0.1051` n `12`; crypto_alt avg `-0.0128` n `230`; crypto_major avg `0.3116` n `8`; equity avg `-0.5797` n `120`; fx avg `0.0861` n `6`; index avg `-0.0254` n `25`; metal avg `0.2825` n `20`; unknown avg `0.1186` n `792`
- 4h: commodity avg `0.0789` n `12`; crypto_alt avg `0.5271` n `230`; crypto_major avg `0.7493` n `8`; equity avg `-0.3181` n `120`; fx avg `-0.0093` n `6`; index avg `0.0471` n `25`; metal avg `0.6382` n `20`; unknown avg `0.3003` n `791`
- 24h: commodity avg `0.308` n `12`; crypto_alt avg `0.616` n `230`; crypto_major avg `1.137` n `8`; equity avg `-1.723` n `120`; fx avg `-0.2` n `6`; index avg `-0.1307` n `25`; metal avg `0.1524` n `20`; unknown avg `0.0236` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
