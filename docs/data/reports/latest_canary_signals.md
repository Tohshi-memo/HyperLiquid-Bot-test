# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T23:52:32.093535+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `0.0934` n `234`; crypto_major avg `0.0868` n `8`; equity avg `0.0072` n `140`; fx avg `0.0065` n `6`; index avg `-0.0109` n `26`; metal avg `0.0117` n `20`; unknown avg `0.038` n `919`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `0.5279` n `234`; crypto_major avg `0.3662` n `8`; equity avg `0.057` n `140`; fx avg `0.0174` n `6`; index avg `-0.0047` n `26`; metal avg `0.0503` n `20`; unknown avg `-0.149` n `917`
- 4h: commodity avg `0.0048` n `12`; crypto_alt avg `0.7091` n `234`; crypto_major avg `0.3887` n `8`; equity avg `0.0328` n `140`; fx avg `0.0113` n `6`; index avg `-0.0561` n `26`; metal avg `0.0202` n `20`; unknown avg `0.6274` n `791`
- 24h: commodity avg `-0.1392` n `12`; crypto_alt avg `3.3993` n `234`; crypto_major avg `1.8746` n `8`; equity avg `1.5798` n `138`; fx avg `0.0213` n `6`; index avg `0.223` n `26`; metal avg `0.5024` n `20`; unknown avg `1.8797` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
