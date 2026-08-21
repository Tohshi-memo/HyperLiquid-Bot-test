# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T20:22:28.323570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `0.3753` n `230`; crypto_major avg `0.4325` n `8`; equity avg `0.0198` n `121`; fx avg `-0.0032` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0383` n `20`; unknown avg `-0.1054` n `793`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `0.7585` n `230`; crypto_major avg `0.4773` n `8`; equity avg `0.0174` n `121`; fx avg `-0.0094` n `6`; index avg `-0.0083` n `25`; metal avg `-0.032` n `20`; unknown avg `-0.0234` n `793`
- 4h: commodity avg `0.0059` n `12`; crypto_alt avg `-0.0958` n `230`; crypto_major avg `0.1037` n `8`; equity avg `-0.0774` n `121`; fx avg `0.0078` n `6`; index avg `-0.0339` n `25`; metal avg `-0.0252` n `20`; unknown avg `-0.1224` n `793`
- 24h: commodity avg `0.1036` n `12`; crypto_alt avg `7.1615` n `230`; crypto_major avg `5.1465` n `8`; equity avg `0.9749` n `121`; fx avg `-0.0827` n `6`; index avg `0.115` n `25`; metal avg `0.5217` n `20`; unknown avg `1.1144` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
