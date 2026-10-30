# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T08:22:30.879478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0841` n `13`; crypto_alt avg `0.3954` n `238`; crypto_major avg `0.3738` n `8`; equity avg `0.0392` n `156`; fx avg `-0.017` n `6`; index avg `-0.0286` n `27`; metal avg `0.0636` n `20`; unknown avg `31.8791` n `1248`
- 1h: commodity avg `0.1064` n `13`; crypto_alt avg `0.0451` n `238`; crypto_major avg `-0.5266` n `8`; equity avg `-0.4365` n `156`; fx avg `0.0139` n `6`; index avg `-0.0353` n `27`; metal avg `-0.012` n `20`; unknown avg `4.4843` n `1190`
- 4h: commodity avg `0.1239` n `13`; crypto_alt avg `0.8268` n `238`; crypto_major avg `-0.2282` n `8`; equity avg `-0.8261` n `156`; fx avg `-0.011` n `6`; index avg `-0.0359` n `27`; metal avg `-0.1669` n `20`; unknown avg `2.6712` n `1172`
- 24h: commodity avg `0.0474` n `13`; crypto_alt avg `-3.0335` n `238`; crypto_major avg `-0.5148` n `8`; equity avg `-3.1554` n `155`; fx avg `0.107` n `6`; index avg `-0.3139` n `27`; metal avg `-0.6941` n `20`; unknown avg `29.9091` n `938`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
