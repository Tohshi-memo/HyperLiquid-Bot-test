# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T08:07:31.048873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `13`; crypto_alt avg `-0.2598` n `239`; crypto_major avg `-0.1216` n `8`; equity avg `0.0427` n `157`; fx avg `0.0174` n `6`; index avg `0.0182` n `27`; metal avg `-0.0035` n `20`; unknown avg `-0.2016` n `1242`
- 1h: commodity avg `-0.118` n `13`; crypto_alt avg `0.1781` n `239`; crypto_major avg `0.2574` n `8`; equity avg `0.4994` n `157`; fx avg `0.0384` n `6`; index avg `0.076` n `27`; metal avg `0.0022` n `20`; unknown avg `0.2495` n `1242`
- 4h: commodity avg `0.3342` n `13`; crypto_alt avg `-0.2261` n `239`; crypto_major avg `0.0137` n `8`; equity avg `-0.1639` n `157`; fx avg `0.054` n `6`; index avg `0.0054` n `27`; metal avg `-0.2587` n `20`; unknown avg `5.241` n `1156`
- 24h: commodity avg `-0.4741` n `13`; crypto_alt avg `-2.668` n `238`; crypto_major avg `-1.6296` n `8`; equity avg `-4.1788` n `157`; fx avg `0.015` n `6`; index avg `-0.3027` n `27`; metal avg `-0.454` n `20`; unknown avg `4.1523` n `1019`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
