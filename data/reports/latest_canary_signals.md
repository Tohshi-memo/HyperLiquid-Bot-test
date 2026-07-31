# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T13:37:28.148580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `-0.0814` n `230`; crypto_major avg `-0.2768` n `8`; equity avg `-0.0859` n `102`; fx avg `-0.1463` n `6`; index avg `0.0464` n `25`; metal avg `-0.0993` n `20`; unknown avg `-0.0959` n `780`
- 1h: commodity avg `0.0191` n `12`; crypto_alt avg `0.3379` n `230`; crypto_major avg `0.1318` n `8`; equity avg `0.422` n `102`; fx avg `-0.1722` n `6`; index avg `0.11` n `25`; metal avg `-0.1934` n `20`; unknown avg `0.3087` n `780`
- 4h: commodity avg `0.2932` n `12`; crypto_alt avg `0.2287` n `230`; crypto_major avg `0.1508` n `8`; equity avg `-0.0217` n `102`; fx avg `-0.1291` n `6`; index avg `0.0313` n `25`; metal avg `-0.1823` n `20`; unknown avg `1.28` n `780`
- 24h: commodity avg `0.5023` n `12`; crypto_alt avg `-0.0858` n `230`; crypto_major avg `-0.103` n `8`; equity avg `4.8653` n `102`; fx avg `-0.0234` n `6`; index avg `0.7979` n `25`; metal avg `-0.2708` n `20`; unknown avg `1.4718` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
