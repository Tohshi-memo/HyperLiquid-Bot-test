# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T22:23:36.219453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.127` n `239`; crypto_major avg `-0.1019` n `8`; equity avg `0.0104` n `158`; fx avg `0.0019` n `6`; index avg `-0.0057` n `27`; metal avg `-0.0015` n `20`; unknown avg `97.0644` n `1264`
- 1h: commodity avg `-0.0211` n `13`; crypto_alt avg `-0.1058` n `239`; crypto_major avg `-0.2304` n `8`; equity avg `0.0513` n `158`; fx avg `-0.0233` n `6`; index avg `0.0169` n `27`; metal avg `0.0256` n `20`; unknown avg `158.439` n `1258`
- 4h: commodity avg `0.2553` n `13`; crypto_alt avg `0.2131` n `239`; crypto_major avg `-0.0769` n `8`; equity avg `0.8379` n `158`; fx avg `-0.0081` n `6`; index avg `0.0664` n `27`; metal avg `-0.0356` n `20`; unknown avg `19.0177` n `1215`
- 24h: commodity avg `0.3887` n `13`; crypto_alt avg `1.0459` n `239`; crypto_major avg `1.2314` n `8`; equity avg `2.41` n `158`; fx avg `0.0682` n `6`; index avg `0.2497` n `27`; metal avg `-0.4925` n `20`; unknown avg `-1.1648` n `1065`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
