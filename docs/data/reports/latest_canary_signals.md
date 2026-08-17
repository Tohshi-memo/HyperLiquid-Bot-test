# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T06:52:28.627820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.1653` n `230`; crypto_major avg `0.2225` n `8`; equity avg `0.0896` n `114`; fx avg `0.0135` n `6`; index avg `0.0042` n `25`; metal avg `0.0701` n `20`; unknown avg `0.0056` n `792`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `0.2421` n `230`; crypto_major avg `0.361` n `8`; equity avg `0.2164` n `114`; fx avg `-0.0004` n `6`; index avg `0.0424` n `25`; metal avg `0.0405` n `20`; unknown avg `0.1462` n `776`
- 4h: commodity avg `-0.1121` n `12`; crypto_alt avg `0.2504` n `230`; crypto_major avg `0.3233` n `8`; equity avg `0.6064` n `114`; fx avg `-0.0036` n `6`; index avg `0.1139` n `25`; metal avg `0.0892` n `20`; unknown avg `0.0553` n `776`
- 24h: commodity avg `-0.2279` n `12`; crypto_alt avg `0.6202` n `230`; crypto_major avg `1.0847` n `8`; equity avg `1.1449` n `114`; fx avg `-0.0207` n `6`; index avg `0.1564` n `25`; metal avg `0.2716` n `20`; unknown avg `0.1654` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
