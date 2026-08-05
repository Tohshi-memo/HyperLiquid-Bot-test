# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T22:52:23.607614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.0019` n `230`; crypto_major avg `-0.0629` n `8`; equity avg `-0.0429` n `108`; fx avg `-0.0011` n `6`; index avg `-0.0058` n `25`; metal avg `-0.0174` n `20`; unknown avg `-0.0047` n `782`
- 1h: commodity avg `-0.0903` n `12`; crypto_alt avg `0.0403` n `230`; crypto_major avg `-0.125` n `8`; equity avg `0.3491` n `108`; fx avg `0.0005` n `6`; index avg `0.0659` n `25`; metal avg `0.0091` n `20`; unknown avg `-0.0266` n `782`
- 4h: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.165` n `230`; crypto_major avg `-0.4794` n `8`; equity avg `-0.7418` n `108`; fx avg `0.0102` n `6`; index avg `-0.052` n `25`; metal avg `-0.048` n `20`; unknown avg `-0.0988` n `782`
- 24h: commodity avg `-0.0425` n `12`; crypto_alt avg `0.3957` n `230`; crypto_major avg `0.5109` n `8`; equity avg `-0.6405` n `108`; fx avg `-0.0392` n `6`; index avg `-0.0691` n `25`; metal avg `0.7857` n `20`; unknown avg `0.7319` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
