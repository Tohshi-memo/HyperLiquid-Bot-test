# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T03:22:27.671237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0523` n `13`; crypto_alt avg `0.4184` n `239`; crypto_major avg `0.2999` n `8`; equity avg `0.0788` n `158`; fx avg `0.0055` n `6`; index avg `0.0116` n `27`; metal avg `0.0072` n `20`; unknown avg `0.1478` n `1265`
- 1h: commodity avg `-0.0716` n `13`; crypto_alt avg `0.4996` n `239`; crypto_major avg `0.1317` n `8`; equity avg `-0.3582` n `158`; fx avg `0.0229` n `6`; index avg `-0.0506` n `27`; metal avg `0.1055` n `20`; unknown avg `0.0735` n `1259`
- 4h: commodity avg `-0.2878` n `13`; crypto_alt avg `0.6168` n `239`; crypto_major avg `0.3973` n `8`; equity avg `-0.6267` n `158`; fx avg `0.0347` n `6`; index avg `-0.1875` n `27`; metal avg `0.4915` n `20`; unknown avg `1.1752` n `1248`
- 24h: commodity avg `-1.7461` n `13`; crypto_alt avg `4.7805` n `239`; crypto_major avg `4.8641` n `8`; equity avg `1.0552` n `158`; fx avg `0.1527` n `6`; index avg `0.4947` n `27`; metal avg `1.9666` n `20`; unknown avg `34.0626` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.252`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1961`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
