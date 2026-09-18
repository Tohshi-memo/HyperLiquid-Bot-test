# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T11:37:32.610224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.047` n `12`; crypto_alt avg `0.3874` n `234`; crypto_major avg `0.201` n `8`; equity avg `0.0164` n `140`; fx avg `-0.0149` n `6`; index avg `0.0198` n `26`; metal avg `0.0092` n `20`; unknown avg `-0.2216` n `925`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `-0.746` n `234`; crypto_major avg `-0.4232` n `8`; equity avg `-0.3046` n `140`; fx avg `-0.0223` n `6`; index avg `-0.0462` n `26`; metal avg `0.0571` n `20`; unknown avg `1.1422` n `923`
- 4h: commodity avg `0.1395` n `12`; crypto_alt avg `0.2784` n `234`; crypto_major avg `0.5453` n `8`; equity avg `-0.4087` n `140`; fx avg `0.0491` n `6`; index avg `-0.0884` n `26`; metal avg `-0.0471` n `20`; unknown avg `0.6561` n `917`
- 24h: commodity avg `-0.1236` n `12`; crypto_alt avg `5.5793` n `234`; crypto_major avg `4.7869` n `8`; equity avg `1.4956` n `140`; fx avg `0.2005` n `6`; index avg `0.1754` n `26`; metal avg `0.6545` n `20`; unknown avg `2.081` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
