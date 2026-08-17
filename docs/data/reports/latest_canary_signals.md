# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T20:52:36.156705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `0.0047` n `230`; crypto_major avg `-0.0095` n `8`; equity avg `0.01` n `114`; fx avg `-0.001` n `6`; index avg `-0.0125` n `25`; metal avg `-0.001` n `20`; unknown avg `0.011` n `792`
- 1h: commodity avg `0.0847` n `12`; crypto_alt avg `0.0114` n `230`; crypto_major avg `0.0352` n `8`; equity avg `-0.0861` n `114`; fx avg `0.0122` n `6`; index avg `-0.0233` n `25`; metal avg `-0.0147` n `20`; unknown avg `-0.0524` n `792`
- 4h: commodity avg `0.4202` n `12`; crypto_alt avg `-0.1353` n `230`; crypto_major avg `-0.1412` n `8`; equity avg `-0.621` n `114`; fx avg `0.0096` n `6`; index avg `-0.137` n `25`; metal avg `-0.0847` n `20`; unknown avg `0.0141` n `792`
- 24h: commodity avg `0.4221` n `12`; crypto_alt avg `0.0787` n `230`; crypto_major avg `0.9518` n `8`; equity avg `1.0031` n `114`; fx avg `0.021` n `6`; index avg `0.0416` n `25`; metal avg `0.2044` n `20`; unknown avg `0.2129` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
