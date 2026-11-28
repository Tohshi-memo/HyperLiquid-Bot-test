# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T17:22:25.046581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `-0.3487` n `239`; crypto_major avg `-0.1832` n `8`; equity avg `-0.0308` n `168`; fx avg `-0.0118` n `6`; index avg `-0.0037` n `27`; metal avg `0.0009` n `20`; unknown avg `3.6462` n `1265`
- 1h: commodity avg `-0.0118` n `13`; crypto_alt avg `-0.0099` n `239`; crypto_major avg `0.1679` n `8`; equity avg `0.0451` n `168`; fx avg `-0.0058` n `6`; index avg `-0.0029` n `27`; metal avg `0.0124` n `20`; unknown avg `57.1117` n `1235`
- 4h: commodity avg `-0.0335` n `13`; crypto_alt avg `-0.8796` n `239`; crypto_major avg `0.1693` n `8`; equity avg `-0.0772` n `168`; fx avg `0.022` n `6`; index avg `-0.0062` n `27`; metal avg `-0.0198` n `20`; unknown avg `42.077` n `1227`
- 24h: commodity avg `-0.1054` n `13`; crypto_alt avg `-3.0453` n `239`; crypto_major avg `-1.174` n `8`; equity avg `0.2296` n `168`; fx avg `-0.0223` n `6`; index avg `0.0162` n `27`; metal avg `0.2505` n `20`; unknown avg `191.8513` n `1080`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
