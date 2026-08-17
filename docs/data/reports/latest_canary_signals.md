# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T07:36:41.254775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `-0.0253` n `230`; crypto_major avg `-0.0254` n `8`; equity avg `0.1134` n `114`; fx avg `0.007` n `6`; index avg `0.0168` n `25`; metal avg `0.1213` n `20`; unknown avg `0.0032` n `792`
- 1h: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.0038` n `230`; crypto_major avg `0.1406` n `8`; equity avg `0.112` n `114`; fx avg `0.0199` n `6`; index avg `-0.0042` n `25`; metal avg `0.1197` n `20`; unknown avg `0.011` n `792`
- 4h: commodity avg `-0.194` n `12`; crypto_alt avg `0.1229` n `230`; crypto_major avg `0.3045` n `8`; equity avg `0.5657` n `114`; fx avg `0.0074` n `6`; index avg `0.0902` n `25`; metal avg `0.1321` n `20`; unknown avg `0.0665` n `776`
- 24h: commodity avg `-0.2579` n `12`; crypto_alt avg `0.1724` n `230`; crypto_major avg `0.8904` n `8`; equity avg `1.1906` n `114`; fx avg `-0.0217` n `6`; index avg `0.14` n `25`; metal avg `0.3288` n `20`; unknown avg `0.1307` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
