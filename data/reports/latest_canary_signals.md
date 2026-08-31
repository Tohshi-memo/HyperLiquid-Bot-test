# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T06:52:23.159973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0471` n `12`; crypto_alt avg `-0.0294` n `232`; crypto_major avg `0.0454` n `8`; equity avg `0.0914` n `128`; fx avg `-0.0068` n `6`; index avg `0.0168` n `26`; metal avg `0.0412` n `20`; unknown avg `0.0575` n `793`
- 1h: commodity avg `-0.0876` n `12`; crypto_alt avg `0.0487` n `232`; crypto_major avg `-0.0433` n `8`; equity avg `0.4895` n `128`; fx avg `-0.0346` n `6`; index avg `0.0858` n `26`; metal avg `0.0803` n `20`; unknown avg `0.1418` n `773`
- 4h: commodity avg `-0.005` n `12`; crypto_alt avg `1.2993` n `231`; crypto_major avg `1.0204` n `8`; equity avg `1.3769` n `128`; fx avg `-0.0569` n `6`; index avg `0.2591` n `26`; metal avg `0.2302` n `20`; unknown avg `0.5685` n `773`
- 24h: commodity avg `0.3784` n `12`; crypto_alt avg `-0.1201` n `231`; crypto_major avg `-1.5105` n `8`; equity avg `-0.1168` n `128`; fx avg `-0.1012` n `6`; index avg `-0.0329` n `26`; metal avg `-0.2044` n `20`; unknown avg `-0.466` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
