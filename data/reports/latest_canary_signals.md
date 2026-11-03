# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T06:22:27.147883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `13`; crypto_alt avg `-0.0727` n `239`; crypto_major avg `0.0523` n `8`; equity avg `-0.0634` n `157`; fx avg `0.0085` n `6`; index avg `-0.0131` n `27`; metal avg `-0.009` n `20`; unknown avg `18.7505` n `1264`
- 1h: commodity avg `0.0569` n `13`; crypto_alt avg `-0.3916` n `239`; crypto_major avg `-0.3386` n `8`; equity avg `-0.3691` n `157`; fx avg `0.0094` n `6`; index avg `-0.0275` n `27`; metal avg `-0.1042` n `20`; unknown avg `0.1178` n `1238`
- 4h: commodity avg `0.2025` n `13`; crypto_alt avg `-0.4048` n `239`; crypto_major avg `-0.4968` n `8`; equity avg `-1.2328` n `157`; fx avg `0.0293` n `6`; index avg `-0.1232` n `27`; metal avg `-0.3878` n `20`; unknown avg `0.2123` n `1168`
- 24h: commodity avg `-0.7978` n `13`; crypto_alt avg `-2.757` n `238`; crypto_major avg `-2.0139` n `8`; equity avg `-4.6579` n `157`; fx avg `0.0224` n `6`; index avg `-0.3551` n `27`; metal avg `-0.387` n `20`; unknown avg `8.2053` n `955`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
