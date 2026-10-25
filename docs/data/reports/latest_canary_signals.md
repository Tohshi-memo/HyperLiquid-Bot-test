# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T05:22:35.382103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0405` n `13`; crypto_alt avg `0.0676` n `237`; crypto_major avg `-0.0033` n `8`; equity avg `0.0248` n `152`; fx avg `0.0005` n `6`; index avg `0.0015` n `26`; metal avg `0.0047` n `20`; unknown avg `-0.2358` n `1231`
- 1h: commodity avg `-0.0566` n `13`; crypto_alt avg `-0.0522` n `237`; crypto_major avg `-0.0172` n `8`; equity avg `0.0206` n `152`; fx avg `0.0044` n `6`; index avg `-0.0019` n `26`; metal avg `0.0244` n `20`; unknown avg `-0.137` n `1231`
- 4h: commodity avg `-0.0746` n `13`; crypto_alt avg `-0.1589` n `237`; crypto_major avg `0.3119` n `8`; equity avg `0.0778` n `152`; fx avg `0.0089` n `6`; index avg `0.0264` n `26`; metal avg `0.0323` n `20`; unknown avg `4.9497` n `1209`
- 24h: commodity avg `-0.0559` n `13`; crypto_alt avg `-1.0877` n `237`; crypto_major avg `0.1635` n `8`; equity avg `0.1002` n `152`; fx avg `-0.0202` n `6`; index avg `0.0058` n `26`; metal avg `-0.052` n `20`; unknown avg `7.5556` n `1060`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
