# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T06:52:27.527349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `13`; crypto_alt avg `0.0132` n `239`; crypto_major avg `0.013` n `8`; equity avg `-0.0175` n `158`; fx avg `-0.0119` n `6`; index avg `0.0022` n `27`; metal avg `0.0052` n `20`; unknown avg `0.7055` n `1259`
- 1h: commodity avg `0.0008` n `13`; crypto_alt avg `-0.129` n `239`; crypto_major avg `-0.0029` n `8`; equity avg `-0.1` n `158`; fx avg `-0.0032` n `6`; index avg `0.0036` n `27`; metal avg `-0.0084` n `20`; unknown avg `0.713` n `1225`
- 4h: commodity avg `-0.0854` n `13`; crypto_alt avg `-0.1117` n `239`; crypto_major avg `-0.1044` n `8`; equity avg `0.0006` n `158`; fx avg `-0.017` n `6`; index avg `0.0056` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.9105` n `1203`
- 24h: commodity avg `-0.2821` n `13`; crypto_alt avg `0.2576` n `239`; crypto_major avg `0.384` n `8`; equity avg `1.1881` n `158`; fx avg `-0.0356` n `6`; index avg `0.1915` n `27`; metal avg `0.2274` n `20`; unknown avg `9.4176` n `1006`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
