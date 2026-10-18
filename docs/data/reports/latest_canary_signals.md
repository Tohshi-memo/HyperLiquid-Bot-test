# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T10:22:26.249433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `13`; crypto_alt avg `-0.1931` n `237`; crypto_major avg `0.006` n `8`; equity avg `-0.0254` n `151`; fx avg `0.002` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.3571` n `1193`
- 1h: commodity avg `0.0769` n `13`; crypto_alt avg `0.0428` n `237`; crypto_major avg `0.2663` n `8`; equity avg `-0.0254` n `151`; fx avg `-0.0026` n `6`; index avg `-0.0019` n `26`; metal avg `0.0161` n `20`; unknown avg `0.0727` n `1191`
- 4h: commodity avg `0.0735` n `13`; crypto_alt avg `0.291` n `237`; crypto_major avg `0.4801` n `8`; equity avg `0.3218` n `151`; fx avg `-0.0019` n `6`; index avg `0.059` n `26`; metal avg `0.0174` n `20`; unknown avg `0.8032` n `1079`
- 24h: commodity avg `0.098` n `13`; crypto_alt avg `-2.2015` n `236`; crypto_major avg `-0.3279` n `8`; equity avg `-0.6382` n `151`; fx avg `-0.0538` n `6`; index avg `-0.0735` n `26`; metal avg `-0.0393` n `20`; unknown avg `4.0274` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1983`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.136`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.128`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0803`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
