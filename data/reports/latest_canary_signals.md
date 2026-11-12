# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T10:14:57.624751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `13`; crypto_alt avg `0.0074` n `239`; crypto_major avg `0.015` n `8`; equity avg `-0.073` n `162`; fx avg `0.0045` n `6`; index avg `-0.0051` n `27`; metal avg `-0.0034` n `20`; unknown avg `0.2006` n `1253`
- 1h: commodity avg `-0.2018` n `13`; crypto_alt avg `0.2643` n `239`; crypto_major avg `0.2602` n `8`; equity avg `0.4252` n `162`; fx avg `-0.0173` n `6`; index avg `0.0446` n `27`; metal avg `0.0546` n `20`; unknown avg `0.6164` n `1253`
- 4h: commodity avg `-0.0304` n `13`; crypto_alt avg `0.0502` n `239`; crypto_major avg `0.0754` n `8`; equity avg `0.6988` n `162`; fx avg `0.081` n `6`; index avg `0.0465` n `27`; metal avg `-0.1878` n `20`; unknown avg `56.3974` n `1231`
- 24h: commodity avg `-0.0603` n `13`; crypto_alt avg `-1.5004` n `239`; crypto_major avg `-0.6315` n `8`; equity avg `-0.5731` n `162`; fx avg `-0.0829` n `6`; index avg `-0.0254` n `27`; metal avg `-0.9201` n `20`; unknown avg `17.7101` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
