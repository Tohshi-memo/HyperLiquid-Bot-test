# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T07:07:29.177898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.0135` n `233`; crypto_major avg `-0.0015` n `8`; equity avg `-0.0502` n `136`; fx avg `0.002` n `6`; index avg `-0.0079` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.0189` n `836`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.2805` n `233`; crypto_major avg `-0.3445` n `8`; equity avg `-0.1932` n `136`; fx avg `-0.0026` n `6`; index avg `-0.0349` n `26`; metal avg `-0.0054` n `20`; unknown avg `-0.1734` n `836`
- 4h: commodity avg `0.1061` n `12`; crypto_alt avg `-0.1271` n `233`; crypto_major avg `-0.4201` n `8`; equity avg `-0.4491` n `136`; fx avg `-0.0054` n `6`; index avg `-0.0712` n `26`; metal avg `-0.0005` n `20`; unknown avg `-0.0361` n `804`
- 24h: commodity avg `0.1875` n `12`; crypto_alt avg `0.637` n `233`; crypto_major avg `-0.2843` n `8`; equity avg `-0.8009` n `136`; fx avg `-0.0111` n `6`; index avg `-0.1358` n `26`; metal avg `0.0224` n `20`; unknown avg `0.4003` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
