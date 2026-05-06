# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T23:22:21.023082+00:00`
- Correlation status: `ready`
- Asset price records: `497`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0279` n `12`; crypto_alt avg `0.2675` n `228`; crypto_major avg `0.2151` n `8`; equity avg `0.1809` n `65`; fx avg `0.0245` n `4`; index avg `0.0285` n `23`; metal avg `-0.0566` n `18`; unknown avg `0.0517` n `356`
- 1h: commodity avg `0.0466` n `12`; crypto_alt avg `-0.1026` n `228`; crypto_major avg `-0.0325` n `8`; equity avg `0.2847` n `65`; fx avg `0.024` n `4`; index avg `0.0377` n `23`; metal avg `-0.0624` n `18`; unknown avg `-0.2823` n `356`
- 4h: commodity avg `0.3819` n `12`; crypto_alt avg `0.0304` n `228`; crypto_major avg `-0.3022` n `8`; equity avg `0.0392` n `65`; fx avg `0.0278` n `4`; index avg `-0.0432` n `23`; metal avg `-0.0658` n `18`; unknown avg `0.0742` n `356`
- 24h: commodity avg `-1.5635` n `7`; crypto_alt avg `1.894` n `223`; crypto_major avg `-0.0308` n `7`; equity avg `1.9285` n `47`; fx avg `-0.5995` n `4`; index avg `1.3974` n `6`; metal avg `2.6621` n `7`; unknown avg `3.4692` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1308`, n `493`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `493`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0963`, n `489`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.085`, n `489`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0815`, n `489`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `489`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.072`, n `489`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `493`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `489`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0586`, n `493`, weak_sample_signal
