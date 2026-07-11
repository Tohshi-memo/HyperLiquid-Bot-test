# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T04:22:26.616267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.0163` n `229`; crypto_major avg `0.0436` n `8`; equity avg `0.0295` n `92`; fx avg `-0.0005` n `6`; index avg `0.0053` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.0078` n `765`
- 1h: commodity avg `0.0114` n `12`; crypto_alt avg `-0.0201` n `229`; crypto_major avg `-0.0136` n `8`; equity avg `0.0084` n `92`; fx avg `-0.0008` n `6`; index avg `0.0044` n `25`; metal avg `-0.0174` n `20`; unknown avg `0.1374` n `763`
- 4h: commodity avg `-0.0548` n `12`; crypto_alt avg `0.2849` n `229`; crypto_major avg `0.0462` n `8`; equity avg `0.052` n `92`; fx avg `0.0006` n `6`; index avg `0.0112` n `25`; metal avg `0.0155` n `20`; unknown avg `1.2517` n `763`
- 24h: commodity avg `-0.4052` n `12`; crypto_alt avg `0.4004` n `229`; crypto_major avg `-0.2806` n `8`; equity avg `-0.7756` n `92`; fx avg `-0.1856` n `6`; index avg `0.0034` n `25`; metal avg `-0.0062` n `20`; unknown avg `4.643` n `730`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
