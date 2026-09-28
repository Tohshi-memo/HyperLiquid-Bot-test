# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T02:22:30.010180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `0.3215` n `234`; crypto_major avg `0.2402` n `8`; equity avg `-0.0001` n `141`; fx avg `-0.0272` n `6`; index avg `0.0007` n `26`; metal avg `0.0443` n `20`; unknown avg `3.7888` n `962`
- 1h: commodity avg `0.0779` n `12`; crypto_alt avg `-0.6279` n `234`; crypto_major avg `-0.5905` n `8`; equity avg `-0.5045` n `141`; fx avg `0.0064` n `6`; index avg `-0.0446` n `26`; metal avg `-0.0125` n `20`; unknown avg `0.1023` n `950`
- 4h: commodity avg `0.0757` n `12`; crypto_alt avg `-0.4363` n `234`; crypto_major avg `-0.7218` n `8`; equity avg `-1.179` n `141`; fx avg `0.0964` n `6`; index avg `-0.0767` n `26`; metal avg `-0.4221` n `20`; unknown avg `2.5095` n `920`
- 24h: commodity avg `-0.3185` n `12`; crypto_alt avg `-0.3357` n `234`; crypto_major avg `-1.1735` n `8`; equity avg `-1.1873` n `141`; fx avg `0.0827` n `6`; index avg `-0.1239` n `26`; metal avg `-0.5685` n `20`; unknown avg `13.2594` n `819`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
