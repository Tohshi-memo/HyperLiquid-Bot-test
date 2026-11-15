# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T22:07:31.787279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `0.1479` n `239`; crypto_major avg `-0.0291` n `8`; equity avg `0.0385` n `162`; fx avg `-0.0117` n `6`; index avg `0.0018` n `27`; metal avg `0.0017` n `20`; unknown avg `0.2064` n `1251`
- 1h: commodity avg `-0.02` n `13`; crypto_alt avg `-0.0652` n `239`; crypto_major avg `0.1244` n `8`; equity avg `0.08` n `162`; fx avg `-0.0221` n `6`; index avg `-0.011` n `27`; metal avg `-0.0144` n `20`; unknown avg `1.7946` n `1253`
- 4h: commodity avg `0.008` n `13`; crypto_alt avg `0.6455` n `239`; crypto_major avg `0.8165` n `8`; equity avg `0.591` n `162`; fx avg `0.0404` n `6`; index avg `0.049` n `27`; metal avg `0.0714` n `20`; unknown avg `41.7789` n `1225`
- 24h: commodity avg `0.0461` n `13`; crypto_alt avg `3.4234` n `239`; crypto_major avg `4.2407` n `8`; equity avg `1.3317` n `162`; fx avg `0.0253` n `6`; index avg `0.1074` n `27`; metal avg `0.2782` n `20`; unknown avg `2.7215` n `1150`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
