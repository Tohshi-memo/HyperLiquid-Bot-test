# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T08:22:26.287227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4501` n `12`; crypto_alt avg `-0.6471` n `229`; crypto_major avg `-0.7113` n `8`; equity avg `-0.5329` n `91`; fx avg `0.0054` n `6`; index avg `-0.1253` n `25`; metal avg `-0.3235` n `20`; unknown avg `-0.0267` n `763`
- 1h: commodity avg `0.4521` n `12`; crypto_alt avg `-0.6427` n `229`; crypto_major avg `-0.4708` n `8`; equity avg `-0.3251` n `91`; fx avg `0.0389` n `6`; index avg `-0.1018` n `25`; metal avg `-0.3163` n `20`; unknown avg `-0.0861` n `763`
- 4h: commodity avg `0.5048` n `12`; crypto_alt avg `-0.8074` n `229`; crypto_major avg `-0.9331` n `8`; equity avg `-0.9053` n `91`; fx avg `-0.0225` n `6`; index avg `-0.2966` n `25`; metal avg `-0.4314` n `20`; unknown avg `-0.2981` n `743`
- 24h: commodity avg `1.1906` n `12`; crypto_alt avg `-3.3407` n `229`; crypto_major avg `-2.9149` n `8`; equity avg `-2.2281` n `91`; fx avg `-0.1673` n `6`; index avg `-0.5081` n `25`; metal avg `-0.577` n `20`; unknown avg `-0.7563` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
