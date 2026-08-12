# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T04:52:25.899243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0536` n `12`; crypto_alt avg `0.078` n `230`; crypto_major avg `0.093` n `8`; equity avg `0.0328` n `113`; fx avg `0.0082` n `6`; index avg `-0.0051` n `25`; metal avg `0.0284` n `20`; unknown avg `0.6048` n `786`
- 1h: commodity avg `-0.1047` n `12`; crypto_alt avg `-0.054` n `230`; crypto_major avg `0.0016` n `8`; equity avg `-0.0004` n `113`; fx avg `-0.0081` n `6`; index avg `-0.0144` n `25`; metal avg `0.0178` n `20`; unknown avg `0.0248` n `786`
- 4h: commodity avg `-0.0127` n `12`; crypto_alt avg `0.0712` n `230`; crypto_major avg `-0.0395` n `8`; equity avg `0.7025` n `113`; fx avg `0.0298` n `6`; index avg `0.1286` n `25`; metal avg `0.1644` n `20`; unknown avg `-0.2604` n `786`
- 24h: commodity avg `0.2395` n `12`; crypto_alt avg `-0.9983` n `230`; crypto_major avg `0.6405` n `8`; equity avg `1.6052` n `113`; fx avg `0.0161` n `6`; index avg `0.0943` n `25`; metal avg `-0.0388` n `20`; unknown avg `-0.0621` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2197`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2093`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1988`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
