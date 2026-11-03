# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T03:07:27.946829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `13`; crypto_alt avg `-0.1412` n `239`; crypto_major avg `-0.1545` n `8`; equity avg `-0.1633` n `157`; fx avg `-0.0211` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0829` n `20`; unknown avg `0.2432` n `1258`
- 1h: commodity avg `0.0516` n `13`; crypto_alt avg `-0.3215` n `239`; crypto_major avg `-0.2398` n `8`; equity avg `-0.383` n `157`; fx avg `-0.0354` n `6`; index avg `-0.0362` n `27`; metal avg `-0.1036` n `20`; unknown avg `0.5645` n `1258`
- 4h: commodity avg `0.077` n `13`; crypto_alt avg `-0.7719` n `239`; crypto_major avg `-0.3174` n `8`; equity avg `0.0545` n `157`; fx avg `-0.0848` n `6`; index avg `0.039` n `27`; metal avg `-0.1759` n `20`; unknown avg `319.4844` n `1250`
- 24h: commodity avg `-0.97` n `13`; crypto_alt avg `-3.5705` n `238`; crypto_major avg `-2.3121` n `8`; equity avg `-3.5338` n `157`; fx avg `-0.0295` n `6`; index avg `-0.1982` n `27`; metal avg `0.0102` n `20`; unknown avg `12.7403` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
