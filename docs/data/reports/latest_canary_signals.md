# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T05:22:33.973775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0684` n `13`; crypto_alt avg `-0.187` n `239`; crypto_major avg `-0.2` n `8`; equity avg `-0.3162` n `161`; fx avg `-0.0174` n `6`; index avg `-0.0397` n `27`; metal avg `-0.0576` n `20`; unknown avg `0.9934` n `1262`
- 1h: commodity avg `0.0876` n `13`; crypto_alt avg `-0.2736` n `239`; crypto_major avg `-0.394` n `8`; equity avg `-0.7981` n `161`; fx avg `-0.013` n `6`; index avg `-0.1058` n `27`; metal avg `-0.0584` n `20`; unknown avg `-0.0631` n `1250`
- 4h: commodity avg `-0.006` n `13`; crypto_alt avg `-0.1445` n `239`; crypto_major avg `-0.2911` n `8`; equity avg `-0.6624` n `161`; fx avg `-0.1418` n `6`; index avg `-0.0537` n `27`; metal avg `-0.1313` n `20`; unknown avg `-0.3855` n `1236`
- 24h: commodity avg `0.144` n `13`; crypto_alt avg `-1.9578` n `239`; crypto_major avg `-0.9439` n `8`; equity avg `-0.4983` n `161`; fx avg `-0.2175` n `6`; index avg `-0.0918` n `27`; metal avg `-0.589` n `20`; unknown avg `-0.2817` n `1127`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
