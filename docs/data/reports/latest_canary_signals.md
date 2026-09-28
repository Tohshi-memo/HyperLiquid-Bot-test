# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T06:37:32.258528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.1132` n `234`; crypto_major avg `-0.0144` n `8`; equity avg `-0.0451` n `141`; fx avg `-0.0092` n `6`; index avg `-0.0278` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.1153` n `962`
- 1h: commodity avg `-0.0801` n `12`; crypto_alt avg `0.1259` n `234`; crypto_major avg `0.1838` n `8`; equity avg `-0.1183` n `141`; fx avg `0.0098` n `6`; index avg `-0.0602` n `26`; metal avg `0.0029` n `20`; unknown avg `3.571` n `936`
- 4h: commodity avg `0.1028` n `12`; crypto_alt avg `-1.961` n `234`; crypto_major avg `-1.0347` n `8`; equity avg `-0.4319` n `141`; fx avg `0.0243` n `6`; index avg `-0.075` n `26`; metal avg `-0.1425` n `20`; unknown avg `1.0339` n `926`
- 24h: commodity avg `-0.3781` n `12`; crypto_alt avg `-2.7683` n `234`; crypto_major avg `-2.3951` n `8`; equity avg `-1.7657` n `141`; fx avg `0.0821` n `6`; index avg `-0.222` n `26`; metal avg `-0.7995` n `20`; unknown avg `3.9672` n `815`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
