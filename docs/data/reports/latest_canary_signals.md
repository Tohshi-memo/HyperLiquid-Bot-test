# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T10:22:21.181402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0976` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `0.0016` n `228`; crypto_major avg `-0.0107` n `8`; equity avg `-0.085` n `74`; fx avg `-0.0018` n `6`; index avg `-0.04` n `23`; metal avg `-0.001` n `18`; unknown avg `1.0388` n `425`
- 1h: commodity avg `-0.1278` n `12`; crypto_alt avg `-1.4837` n `228`; crypto_major avg `-1.2121` n `8`; equity avg `-1.9141` n `74`; fx avg `0.0113` n `6`; index avg `-0.4109` n `23`; metal avg `-0.114` n `18`; unknown avg `0.8581` n `425`
- 4h: commodity avg `-0.0844` n `12`; crypto_alt avg `-0.7947` n `228`; crypto_major avg `-1.2109` n `8`; equity avg `-0.6533` n `74`; fx avg `-0.005` n `6`; index avg `-0.1133` n `23`; metal avg `-0.0406` n `18`; unknown avg `1.3418` n `425`
- 24h: commodity avg `-1.2695` n `12`; crypto_alt avg `-4.6964` n `228`; crypto_major avg `-4.1652` n `8`; equity avg `-7.1964` n `74`; fx avg `-0.2578` n `6`; index avg `-4.198` n `23`; metal avg `-4.4636` n `18`; unknown avg `0.337` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
