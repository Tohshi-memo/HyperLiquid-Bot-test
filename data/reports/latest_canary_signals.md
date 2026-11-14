# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T12:52:37.891948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.2511` n `239`; crypto_major avg `-0.2594` n `8`; equity avg `-0.018` n `162`; fx avg `0.0068` n `6`; index avg `-0.0022` n `27`; metal avg `-0.0035` n `20`; unknown avg `158.35` n `1262`
- 1h: commodity avg `-0.0139` n `13`; crypto_alt avg `-0.3736` n `239`; crypto_major avg `-0.382` n `8`; equity avg `-0.0579` n `162`; fx avg `0.0095` n `6`; index avg `-0.0028` n `27`; metal avg `-0.006` n `20`; unknown avg `0.0076` n `1254`
- 4h: commodity avg `-0.052` n `13`; crypto_alt avg `-0.2911` n `239`; crypto_major avg `0.1131` n `8`; equity avg `0.0281` n `162`; fx avg `-0.003` n `6`; index avg `-0.0042` n `27`; metal avg `0.0131` n `20`; unknown avg `85.0172` n `1178`
- 24h: commodity avg `-0.2772` n `13`; crypto_alt avg `-3.6549` n `239`; crypto_major avg `-3.8856` n `8`; equity avg `-2.7176` n `162`; fx avg `-0.1178` n `6`; index avg `-0.2363` n `27`; metal avg `-0.3624` n `20`; unknown avg `1.8056` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
