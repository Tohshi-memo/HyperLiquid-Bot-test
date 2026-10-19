# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T02:52:27.375010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `0.1863` n `237`; crypto_major avg `0.2949` n `8`; equity avg `0.1063` n `151`; fx avg `0.0246` n `6`; index avg `0.0043` n `26`; metal avg `0.0061` n `20`; unknown avg `-0.3708` n `1194`
- 1h: commodity avg `-0.0173` n `13`; crypto_alt avg `0.0916` n `237`; crypto_major avg `0.2742` n `8`; equity avg `0.43` n `151`; fx avg `-0.0263` n `6`; index avg `0.0558` n `26`; metal avg `0.0125` n `20`; unknown avg `-0.3051` n `1192`
- 4h: commodity avg `-0.0863` n `13`; crypto_alt avg `1.3519` n `237`; crypto_major avg `1.0733` n `8`; equity avg `1.653` n `151`; fx avg `-0.0292` n `6`; index avg `0.252` n `26`; metal avg `0.0924` n `20`; unknown avg `1.118` n `1128`
- 24h: commodity avg `-0.424` n `13`; crypto_alt avg `0.1452` n `237`; crypto_major avg `0.9171` n `8`; equity avg `2.7336` n `151`; fx avg `-0.0405` n `6`; index avg `0.4884` n `26`; metal avg `0.2715` n `20`; unknown avg `3.0337` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2022`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1075`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0957`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0618`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0613`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
