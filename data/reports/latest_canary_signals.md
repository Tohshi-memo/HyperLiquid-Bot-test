# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T06:52:24.191063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.645` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0591` n `13`; crypto_alt avg `0.0454` n `239`; crypto_major avg `0.113` n `8`; equity avg `0.0818` n `164`; fx avg `-0.0032` n `6`; index avg `0.0102` n `27`; metal avg `-0.0116` n `20`; unknown avg `0.7757` n `1266`
- 1h: commodity avg `-0.0856` n `13`; crypto_alt avg `0.406` n `239`; crypto_major avg `0.5131` n `8`; equity avg `0.7465` n `164`; fx avg `-0.0179` n `6`; index avg `0.1075` n `27`; metal avg `-0.0995` n `20`; unknown avg `17.6019` n `1230`
- 4h: commodity avg `-0.0492` n `13`; crypto_alt avg `0.981` n `239`; crypto_major avg `1.7834` n `8`; equity avg `1.1017` n `164`; fx avg `0.0028` n `6`; index avg `0.2046` n `27`; metal avg `0.1384` n `20`; unknown avg `722.4923` n `1207`
- 24h: commodity avg `0.2452` n `13`; crypto_alt avg `0.1393` n `239`; crypto_major avg `-0.2432` n `8`; equity avg `0.1412` n `164`; fx avg `-0.1176` n `6`; index avg `0.16` n `27`; metal avg `-0.4304` n `20`; unknown avg `932.7775` n `1105`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
