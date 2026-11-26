# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T16:07:29.519282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `13`; crypto_alt avg `0.2022` n `239`; crypto_major avg `0.2686` n `8`; equity avg `0.0827` n `168`; fx avg `0.0079` n `6`; index avg `0.0152` n `27`; metal avg `0.0243` n `20`; unknown avg `0.3705` n `1249`
- 1h: commodity avg `0.0448` n `13`; crypto_alt avg `0.9501` n `239`; crypto_major avg `1.1009` n `8`; equity avg `0.3673` n `168`; fx avg `0.0068` n `6`; index avg `0.0257` n `27`; metal avg `-0.0131` n `20`; unknown avg `1.1652` n `1251`
- 4h: commodity avg `0.1924` n `13`; crypto_alt avg `-0.4976` n `239`; crypto_major avg `-0.2906` n `8`; equity avg `-0.0519` n `168`; fx avg `0.0104` n `6`; index avg `-0.0183` n `27`; metal avg `-0.0165` n `20`; unknown avg `8.2109` n `1245`
- 24h: commodity avg `0.2098` n `13`; crypto_alt avg `5.0064` n `239`; crypto_major avg `4.046` n `8`; equity avg `6.876` n `168`; fx avg `0.058` n `6`; index avg `0.6481` n `27`; metal avg `1.4378` n `20`; unknown avg `15.488` n `1056`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
