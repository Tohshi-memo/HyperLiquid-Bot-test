# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T11:52:29.782981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `0.0857` n `239`; crypto_major avg `0.176` n `8`; equity avg `0.1481` n `162`; fx avg `0.0068` n `6`; index avg `0.0201` n `27`; metal avg `0.0754` n `20`; unknown avg `0.536` n `1262`
- 1h: commodity avg `-0.0497` n `13`; crypto_alt avg `0.1198` n `239`; crypto_major avg `0.2503` n `8`; equity avg `0.2431` n `162`; fx avg `0.0383` n `6`; index avg `0.0224` n `27`; metal avg `0.1007` n `20`; unknown avg `39.6661` n `1256`
- 4h: commodity avg `0.0557` n `13`; crypto_alt avg `0.0579` n `239`; crypto_major avg `0.9633` n `8`; equity avg `0.4331` n `162`; fx avg `-0.0076` n `6`; index avg `0.0548` n `27`; metal avg `0.0052` n `20`; unknown avg `43.7274` n `1148`
- 24h: commodity avg `0.6909` n `13`; crypto_alt avg `0.018` n `239`; crypto_major avg `-1.3989` n `8`; equity avg `-0.5781` n `162`; fx avg `-0.0161` n `6`; index avg `0.0734` n `27`; metal avg `-0.2908` n `20`; unknown avg `0.4667` n `1073`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
