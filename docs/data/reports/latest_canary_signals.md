# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T13:52:30.722186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `-0.2093` n `239`; crypto_major avg `-0.1324` n `8`; equity avg `-0.1375` n `157`; fx avg `-0.0087` n `6`; index avg `-0.0009` n `27`; metal avg `0.0764` n `20`; unknown avg `0.5531` n `1262`
- 1h: commodity avg `-0.5515` n `13`; crypto_alt avg `-0.2535` n `239`; crypto_major avg `-0.0922` n `8`; equity avg `0.495` n `157`; fx avg `-0.0176` n `6`; index avg `0.1036` n `27`; metal avg `0.2485` n `20`; unknown avg `2.9381` n `1256`
- 4h: commodity avg `-0.7097` n `13`; crypto_alt avg `1.3903` n `239`; crypto_major avg `0.9548` n `8`; equity avg `1.0302` n `157`; fx avg `-0.0353` n `6`; index avg `0.159` n `27`; metal avg `0.5159` n `20`; unknown avg `167.4273` n `1222`
- 24h: commodity avg `-0.8159` n `13`; crypto_alt avg `-0.7746` n `239`; crypto_major avg `-0.2011` n `8`; equity avg `-2.3054` n `157`; fx avg `-0.0163` n `6`; index avg `-0.089` n `27`; metal avg `-0.1084` n `20`; unknown avg `0.1577` n `1020`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
