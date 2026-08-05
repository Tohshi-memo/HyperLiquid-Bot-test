# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T17:52:58.173689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.525` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0141` n `12`; crypto_alt avg `0.1269` n `230`; crypto_major avg `0.1773` n `8`; equity avg `-0.0074` n `108`; fx avg `-0.0083` n `6`; index avg `0.0164` n `25`; metal avg `0.0267` n `20`; unknown avg `-0.071` n `782`
- 1h: commodity avg `-0.0228` n `12`; crypto_alt avg `0.3541` n `230`; crypto_major avg `0.4518` n `8`; equity avg `-0.0749` n `108`; fx avg `-0.0001` n `6`; index avg `-0.001` n `25`; metal avg `0.0681` n `20`; unknown avg `-0.1374` n `782`
- 4h: commodity avg `-0.1672` n `12`; crypto_alt avg `0.5068` n `230`; crypto_major avg `0.9246` n `8`; equity avg `-0.6004` n `108`; fx avg `-0.0134` n `6`; index avg `-0.1544` n `25`; metal avg `0.2225` n `20`; unknown avg `0.0411` n `782`
- 24h: commodity avg `-0.1401` n `12`; crypto_alt avg `1.011` n `230`; crypto_major avg `1.2303` n `8`; equity avg `-0.1446` n `108`; fx avg `-0.0006` n `6`; index avg `0.0004` n `25`; metal avg `0.7076` n `20`; unknown avg `0.8193` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
