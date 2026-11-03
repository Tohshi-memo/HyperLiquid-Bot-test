# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T21:40:02.216358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0295` n `13`; crypto_alt avg `0.0939` n `239`; crypto_major avg `0.0318` n `8`; equity avg `0.2327` n `158`; fx avg `0.0011` n `6`; index avg `0.0295` n `27`; metal avg `0.0204` n `20`; unknown avg `0.0558` n `1262`
- 1h: commodity avg `0.0478` n `13`; crypto_alt avg `0.4914` n `239`; crypto_major avg `0.3745` n `8`; equity avg `1.0606` n `158`; fx avg `0.0103` n `6`; index avg `0.1242` n `27`; metal avg `0.0729` n `20`; unknown avg `-0.8202` n `1231`
- 4h: commodity avg `0.2212` n `13`; crypto_alt avg `0.4373` n `239`; crypto_major avg `0.2935` n `8`; equity avg `1.0366` n `158`; fx avg `0.0225` n `6`; index avg `0.1005` n `27`; metal avg `0.0005` n `20`; unknown avg `-0.772` n `1175`
- 24h: commodity avg `0.3854` n `13`; crypto_alt avg `1.3038` n `239`; crypto_major avg `1.5782` n `8`; equity avg `2.6235` n `158`; fx avg `0.0827` n `6`; index avg `0.2531` n `27`; metal avg `-0.463` n `20`; unknown avg `21.4347` n `1065`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
