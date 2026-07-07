# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T19:07:34.560568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1862` n `12`; crypto_alt avg `-0.4239` n `229`; crypto_major avg `-0.2974` n `8`; equity avg `-0.1932` n `91`; fx avg `0.005` n `6`; index avg `-0.0504` n `25`; metal avg `-0.2012` n `20`; unknown avg `0.9139` n `763`
- 1h: commodity avg `0.2725` n `12`; crypto_alt avg `-1.0871` n `229`; crypto_major avg `-1.0302` n `8`; equity avg `-0.8907` n `91`; fx avg `-0.0057` n `6`; index avg `-0.1536` n `25`; metal avg `-0.3854` n `20`; unknown avg `0.4772` n `763`
- 4h: commodity avg `0.3183` n `12`; crypto_alt avg `-0.9298` n `229`; crypto_major avg `-0.5812` n `8`; equity avg `-0.0113` n `91`; fx avg `-0.0586` n `6`; index avg `0.0511` n `25`; metal avg `-0.3844` n `20`; unknown avg `-0.1599` n `755`
- 24h: commodity avg `0.7935` n `12`; crypto_alt avg `-2.0367` n `229`; crypto_major avg `-1.2488` n `8`; equity avg `-3.3234` n `91`; fx avg `-0.2509` n `6`; index avg `-0.6315` n `25`; metal avg `-0.5741` n `20`; unknown avg `-0.4986` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
