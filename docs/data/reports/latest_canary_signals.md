# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T07:07:31.154290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0972` n `12`; crypto_alt avg `-0.0312` n `230`; crypto_major avg `-0.0401` n `8`; equity avg `0.0453` n `108`; fx avg `0.009` n `6`; index avg `0.0009` n `25`; metal avg `-0.0101` n `20`; unknown avg `0.0763` n `781`
- 1h: commodity avg `0.0721` n `12`; crypto_alt avg `0.0054` n `230`; crypto_major avg `-0.0196` n `8`; equity avg `-0.1771` n `108`; fx avg `0.034` n `6`; index avg `-0.0356` n `25`; metal avg `0.1131` n `20`; unknown avg `0.1527` n `781`
- 4h: commodity avg `0.209` n `12`; crypto_alt avg `0.1284` n `230`; crypto_major avg `-0.0418` n `8`; equity avg `0.3721` n `108`; fx avg `0.0779` n `6`; index avg `0.0317` n `25`; metal avg `0.2888` n `20`; unknown avg `0.1285` n `749`
- 24h: commodity avg `-1.1938` n `12`; crypto_alt avg `0.9133` n `230`; crypto_major avg `1.0006` n `8`; equity avg `3.478` n `108`; fx avg `0.0097` n `6`; index avg `0.7249` n `25`; metal avg `1.3033` n `20`; unknown avg `0.5927` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
