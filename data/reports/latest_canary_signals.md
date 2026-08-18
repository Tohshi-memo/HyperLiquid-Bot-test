# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T08:37:33.468383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0902` n `12`; crypto_alt avg `0.1434` n `230`; crypto_major avg `0.1971` n `8`; equity avg `0.234` n `114`; fx avg `-0.0144` n `6`; index avg `0.0318` n `25`; metal avg `0.0442` n `20`; unknown avg `0.0134` n `795`
- 1h: commodity avg `-0.0093` n `12`; crypto_alt avg `0.1259` n `230`; crypto_major avg `-0.0651` n `8`; equity avg `-0.5312` n `114`; fx avg `0.0009` n `6`; index avg `-0.0539` n `25`; metal avg `-0.0664` n `20`; unknown avg `0.006` n `795`
- 4h: commodity avg `-0.0758` n `12`; crypto_alt avg `0.4061` n `230`; crypto_major avg `0.1513` n `8`; equity avg `-0.8857` n `114`; fx avg `-0.0171` n `6`; index avg `-0.153` n `25`; metal avg `-0.0224` n `20`; unknown avg `0.0175` n `761`
- 24h: commodity avg `0.5804` n `12`; crypto_alt avg `-0.6641` n `230`; crypto_major avg `0.2748` n `8`; equity avg `-2.4234` n `114`; fx avg `-0.0139` n `6`; index avg `-0.4959` n `25`; metal avg `-0.2598` n `20`; unknown avg `0.032` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
