# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T14:22:31.212986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0472` n `12`; crypto_alt avg `0.1568` n `228`; crypto_major avg `0.0459` n `8`; equity avg `0.4112` n `88`; fx avg `0.0275` n `6`; index avg `0.0291` n `23`; metal avg `0.3571` n `20`; unknown avg `-0.16` n `765`
- 1h: commodity avg `-0.0086` n `12`; crypto_alt avg `1.0419` n `228`; crypto_major avg `0.9116` n `8`; equity avg `1.064` n `88`; fx avg `0.0299` n `6`; index avg `0.1782` n `23`; metal avg `0.373` n `20`; unknown avg `0.1642` n `765`
- 4h: commodity avg `0.0996` n `12`; crypto_alt avg `-0.275` n `228`; crypto_major avg `-0.3412` n `8`; equity avg `0.5816` n `88`; fx avg `0.025` n `6`; index avg `0.211` n `23`; metal avg `0.2906` n `20`; unknown avg `-0.3435` n `765`
- 24h: commodity avg `0.3153` n `12`; crypto_alt avg `-0.4217` n `228`; crypto_major avg `0.4046` n `8`; equity avg `3.55` n `88`; fx avg `0.1108` n `6`; index avg `0.5837` n `23`; metal avg `0.6588` n `20`; unknown avg `7.892` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
