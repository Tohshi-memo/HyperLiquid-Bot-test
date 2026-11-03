# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T09:07:28.991808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `13`; crypto_alt avg `0.295` n `239`; crypto_major avg `0.3816` n `8`; equity avg `0.6057` n `157`; fx avg `0.0109` n `6`; index avg `0.0505` n `27`; metal avg `0.032` n `20`; unknown avg `0.6175` n `1248`
- 1h: commodity avg `0.1603` n `13`; crypto_alt avg `0.361` n `239`; crypto_major avg `0.2381` n `8`; equity avg `0.4449` n `157`; fx avg `0.0334` n `6`; index avg `0.0379` n `27`; metal avg `-0.151` n `20`; unknown avg `0.862` n `1248`
- 4h: commodity avg `0.403` n `13`; crypto_alt avg `-0.0023` n `239`; crypto_major avg `0.207` n `8`; equity avg `0.5345` n `157`; fx avg `0.0769` n `6`; index avg `0.0714` n `27`; metal avg `-0.3481` n `20`; unknown avg `0.9435` n `1206`
- 24h: commodity avg `-0.2095` n `13`; crypto_alt avg `-2.3976` n `238`; crypto_major avg `-1.6635` n `8`; equity avg `-3.8535` n `157`; fx avg `-0.0023` n `6`; index avg `-0.268` n `27`; metal avg `-0.5775` n `20`; unknown avg `3.9966` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
