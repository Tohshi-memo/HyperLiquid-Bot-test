# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T01:37:28.086211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0222` n `12`; crypto_alt avg `-0.1798` n `234`; crypto_major avg `-0.1738` n `8`; equity avg `-0.0871` n `141`; fx avg `0.0183` n `6`; index avg `0.0311` n `26`; metal avg `-0.0452` n `20`; unknown avg `-0.1195` n `952`
- 1h: commodity avg `0.0365` n `12`; crypto_alt avg `-0.3684` n `234`; crypto_major avg `-0.2169` n `8`; equity avg `-0.4851` n `141`; fx avg `0.0321` n `6`; index avg `-0.0428` n `26`; metal avg `-0.252` n `20`; unknown avg `25.4907` n `950`
- 4h: commodity avg `-0.3642` n `12`; crypto_alt avg `-0.1978` n `234`; crypto_major avg `-0.4091` n `8`; equity avg `-1.0482` n `141`; fx avg `0.1367` n `6`; index avg `-0.104` n `26`; metal avg `-0.587` n `20`; unknown avg `2.897` n `910`
- 24h: commodity avg `-0.4125` n `12`; crypto_alt avg `0.4326` n `234`; crypto_major avg `-0.3625` n `8`; equity avg `-0.6996` n `141`; fx avg `0.0947` n `6`; index avg `-0.0508` n `26`; metal avg `-0.6008` n `20`; unknown avg `12.1736` n `819`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
