# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T23:07:32.223813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.0603` n `234`; crypto_major avg `0.1038` n `8`; equity avg `0.0017` n `137`; fx avg `0.0065` n `6`; index avg `-0.0073` n `27`; metal avg `-0.0125` n `20`; unknown avg `0.0467` n `917`
- 1h: commodity avg `0.0364` n `12`; crypto_alt avg `0.5781` n `234`; crypto_major avg `0.477` n `8`; equity avg `0.0592` n `137`; fx avg `0.0131` n `6`; index avg `0.0072` n `27`; metal avg `-0.0116` n `20`; unknown avg `0.9948` n `909`
- 4h: commodity avg `0.0434` n `12`; crypto_alt avg `-0.734` n `234`; crypto_major avg `-0.5802` n `8`; equity avg `-0.0588` n `137`; fx avg `0.0057` n `6`; index avg `0.0304` n `27`; metal avg `-0.0575` n `20`; unknown avg `1.3409` n `845`
- 24h: commodity avg `0.4864` n `12`; crypto_alt avg `-3.753` n `234`; crypto_major avg `-4.0649` n `8`; equity avg `-1.299` n `137`; fx avg `0.2503` n `6`; index avg `-0.0576` n `27`; metal avg `0.18` n `20`; unknown avg `2.0039` n `802`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
