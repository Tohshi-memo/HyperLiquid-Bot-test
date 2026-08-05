# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T05:37:29.590206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0802` n `12`; crypto_alt avg `0.0117` n `230`; crypto_major avg `-0.0546` n `8`; equity avg `-0.1061` n `108`; fx avg `-0.0163` n `6`; index avg `-0.0124` n `25`; metal avg `0.1101` n `20`; unknown avg `-0.0069` n `781`
- 1h: commodity avg `-0.0579` n `12`; crypto_alt avg `0.149` n `230`; crypto_major avg `0.3207` n `8`; equity avg `0.2232` n `108`; fx avg `0.017` n `6`; index avg `0.023` n `25`; metal avg `0.1122` n `20`; unknown avg `0.5894` n `781`
- 4h: commodity avg `-0.2392` n `12`; crypto_alt avg `0.381` n `230`; crypto_major avg `0.3908` n `8`; equity avg `0.8279` n `108`; fx avg `0.0118` n `6`; index avg `0.0656` n `25`; metal avg `0.4874` n `20`; unknown avg `0.457` n `781`
- 24h: commodity avg `-1.5339` n `12`; crypto_alt avg `0.6067` n `230`; crypto_major avg `0.8189` n `8`; equity avg `3.922` n `108`; fx avg `0.0183` n `6`; index avg `0.7759` n `25`; metal avg `1.1451` n `20`; unknown avg `0.4817` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
