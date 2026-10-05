# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T18:22:34.606432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `13`; crypto_alt avg `0.0665` n `235`; crypto_major avg `0.0275` n `8`; equity avg `-0.0065` n `144`; fx avg `-0.0049` n `6`; index avg `0.0072` n `26`; metal avg `-0.0243` n `20`; unknown avg `1.2709` n `1079`
- 1h: commodity avg `-0.0102` n `13`; crypto_alt avg `0.4157` n `235`; crypto_major avg `0.2378` n `8`; equity avg `0.1414` n `144`; fx avg `0.0085` n `6`; index avg `0.0183` n `26`; metal avg `0.0513` n `20`; unknown avg `0.9495` n `1077`
- 4h: commodity avg `0.06` n `13`; crypto_alt avg `-0.5928` n `235`; crypto_major avg `-0.5388` n `8`; equity avg `0.1875` n `144`; fx avg `0.0517` n `6`; index avg `0.051` n `26`; metal avg `-0.0336` n `20`; unknown avg `1.088` n `1013`
- 24h: commodity avg `-0.3309` n `13`; crypto_alt avg `0.1995` n `235`; crypto_major avg `0.2884` n `8`; equity avg `0.3658` n `144`; fx avg `-0.0838` n `6`; index avg `0.1282` n `26`; metal avg `0.1671` n `20`; unknown avg `-0.0261` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2009`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
