# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T09:37:27.544960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.2231` n `229`; crypto_major avg `-0.1545` n `8`; equity avg `-0.0251` n `88`; fx avg `0.0` n `6`; index avg `-0.0152` n `25`; metal avg `0.0002` n `20`; unknown avg `0.0695` n `765`
- 1h: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.113` n `229`; crypto_major avg `-0.2732` n `8`; equity avg `-0.1099` n `88`; fx avg `-0.0015` n `6`; index avg `-0.0055` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.0145` n `765`
- 4h: commodity avg `0.0259` n `12`; crypto_alt avg `-0.0216` n `229`; crypto_major avg `0.0017` n `8`; equity avg `-0.0445` n `88`; fx avg `0.0102` n `6`; index avg `-0.018` n `25`; metal avg `0.0218` n `20`; unknown avg `-0.1032` n `731`
- 24h: commodity avg `0.0449` n `12`; crypto_alt avg `-0.261` n `229`; crypto_major avg `-0.6066` n `8`; equity avg `0.1846` n `88`; fx avg `0.0172` n `6`; index avg `0.0526` n `25`; metal avg `0.0752` n `20`; unknown avg `-1.2133` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
