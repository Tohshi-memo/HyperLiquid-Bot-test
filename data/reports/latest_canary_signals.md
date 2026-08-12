# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T06:07:34.687266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.0144` n `230`; crypto_major avg `-0.1009` n `8`; equity avg `0.0643` n `113`; fx avg `-0.0051` n `6`; index avg `-0.0001` n `25`; metal avg `0.013` n `20`; unknown avg `0.0056` n `770`
- 1h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.0482` n `230`; crypto_major avg `0.0148` n `8`; equity avg `0.0073` n `113`; fx avg `-0.0028` n `6`; index avg `0.0203` n `25`; metal avg `-0.0777` n `20`; unknown avg `-0.0047` n `770`
- 4h: commodity avg `0.0642` n `12`; crypto_alt avg `-0.2216` n `230`; crypto_major avg `-0.3359` n `8`; equity avg `0.3905` n `113`; fx avg `-0.0019` n `6`; index avg `0.0869` n `25`; metal avg `0.0261` n `20`; unknown avg `-0.0151` n `770`
- 24h: commodity avg `0.2366` n `12`; crypto_alt avg `-1.0085` n `230`; crypto_major avg `0.6466` n `8`; equity avg `1.8105` n `113`; fx avg `-0.0007` n `6`; index avg `0.1529` n `25`; metal avg `0.015` n `20`; unknown avg `-0.0567` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2175`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2171`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2159`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
