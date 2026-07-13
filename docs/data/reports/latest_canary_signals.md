# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T17:22:25.065039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0833` n `12`; crypto_alt avg `-0.0664` n `230`; crypto_major avg `0.0847` n `8`; equity avg `-0.1139` n `92`; fx avg `-0.0127` n `6`; index avg `-0.0063` n `25`; metal avg `0.0314` n `20`; unknown avg `-0.0317` n `766`
- 1h: commodity avg `0.2121` n `12`; crypto_alt avg `-0.2147` n `230`; crypto_major avg `-0.0144` n `8`; equity avg `-0.2695` n `92`; fx avg `0.0074` n `6`; index avg `-0.0032` n `25`; metal avg `-0.1101` n `20`; unknown avg `-0.0257` n `766`
- 4h: commodity avg `0.6639` n `12`; crypto_alt avg `-0.3108` n `230`; crypto_major avg `-0.1493` n `8`; equity avg `-0.7745` n `92`; fx avg `-0.0195` n `6`; index avg `-0.1055` n `25`; metal avg `-0.3721` n `20`; unknown avg `-0.0608` n `766`
- 24h: commodity avg `0.3129` n `12`; crypto_alt avg `-1.9104` n `230`; crypto_major avg `-2.7349` n `8`; equity avg `-2.9732` n `92`; fx avg `-0.0819` n `6`; index avg `-0.5698` n `25`; metal avg `-0.5103` n `20`; unknown avg `-0.1113` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1987`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
