# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T07:37:33.943582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.1362` n `239`; crypto_major avg `0.0436` n `8`; equity avg `0.1577` n `157`; fx avg `-0.0017` n `6`; index avg `0.0124` n `27`; metal avg `-0.026` n `20`; unknown avg `0.463` n `1264`
- 1h: commodity avg `0.2116` n `13`; crypto_alt avg `0.0209` n `239`; crypto_major avg `0.0306` n `8`; equity avg `-0.0958` n `157`; fx avg `-0.0029` n `6`; index avg `-0.0342` n `27`; metal avg `-0.1532` n `20`; unknown avg `0.4956` n `1254`
- 4h: commodity avg `0.3619` n `13`; crypto_alt avg `0.2471` n `239`; crypto_major avg `0.3332` n `8`; equity avg `-0.5127` n `157`; fx avg `0.0326` n `6`; index avg `-0.088` n `27`; metal avg `-0.3121` n `20`; unknown avg `0.3328` n `1164`
- 24h: commodity avg `-0.5189` n `13`; crypto_alt avg `-2.299` n `238`; crypto_major avg `-1.2881` n `8`; equity avg `-4.3202` n `157`; fx avg `-0.0225` n `6`; index avg `-0.3393` n `27`; metal avg `-0.4614` n `20`; unknown avg `8.8235` n `949`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
