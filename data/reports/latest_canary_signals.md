# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T19:22:25.917278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0394` n `12`; crypto_alt avg `-0.4182` n `233`; crypto_major avg `-0.3022` n `8`; equity avg `-0.087` n `136`; fx avg `-0.0007` n `6`; index avg `-0.0129` n `27`; metal avg `-0.0306` n `20`; unknown avg `2.9863` n `840`
- 1h: commodity avg `0.0517` n `12`; crypto_alt avg `-0.3026` n `233`; crypto_major avg `-0.16` n `8`; equity avg `-0.0474` n `136`; fx avg `0.0058` n `6`; index avg `-0.0164` n `27`; metal avg `-0.0181` n `20`; unknown avg `1.1957` n `830`
- 4h: commodity avg `0.0496` n `12`; crypto_alt avg `0.2801` n `233`; crypto_major avg `0.4825` n `8`; equity avg `0.2701` n `136`; fx avg `-0.0011` n `6`; index avg `-0.008` n `27`; metal avg `0.0014` n `20`; unknown avg `2.206` n `766`
- 24h: commodity avg `0.2943` n `12`; crypto_alt avg `-0.0163` n `233`; crypto_major avg `-0.6812` n `8`; equity avg `-1.4047` n `136`; fx avg `0.0149` n `6`; index avg `-0.2718` n `26`; metal avg `-0.0921` n `20`; unknown avg `2.728` n `720`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
