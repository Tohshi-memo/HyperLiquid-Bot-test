# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T03:52:34.302734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0393` n `13`; crypto_alt avg `0.2797` n `239`; crypto_major avg `0.3114` n `8`; equity avg `0.2845` n `164`; fx avg `0.0086` n `6`; index avg `0.0537` n `27`; metal avg `0.0619` n `20`; unknown avg `237.5167` n `1264`
- 1h: commodity avg `-0.0507` n `13`; crypto_alt avg `0.6744` n `239`; crypto_major avg `0.6671` n `8`; equity avg `0.3621` n `164`; fx avg `-0.0037` n `6`; index avg `0.0785` n `27`; metal avg `-0.0318` n `20`; unknown avg `11.0465` n `1253`
- 4h: commodity avg `0.0088` n `13`; crypto_alt avg `0.2681` n `239`; crypto_major avg `-0.0728` n `8`; equity avg `0.1555` n `164`; fx avg `-0.045` n `6`; index avg `0.0348` n `27`; metal avg `-0.2164` n `20`; unknown avg `2.477` n `1247`
- 24h: commodity avg `0.0499` n `13`; crypto_alt avg `-0.0933` n `239`; crypto_major avg `-1.3946` n `8`; equity avg `-0.3128` n `164`; fx avg `-0.116` n `6`; index avg `0.0636` n `27`; metal avg `-0.7191` n `20`; unknown avg `126.3484` n `1121`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
