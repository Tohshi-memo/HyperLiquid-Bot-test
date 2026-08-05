# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T07:22:56.172006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0967` n `12`; crypto_alt avg `-0.1767` n `230`; crypto_major avg `-0.2911` n `8`; equity avg `-0.212` n `108`; fx avg `-0.0139` n `6`; index avg `-0.0284` n `25`; metal avg `-0.0094` n `20`; unknown avg `-0.0622` n `781`
- 1h: commodity avg `0.1882` n `12`; crypto_alt avg `-0.1626` n `230`; crypto_major avg `-0.2848` n `8`; equity avg `-0.1963` n `108`; fx avg `0.0106` n `6`; index avg `-0.0308` n `25`; metal avg `0.0637` n `20`; unknown avg `-0.0209` n `781`
- 4h: commodity avg `0.3192` n `12`; crypto_alt avg `0.3037` n `230`; crypto_major avg `0.101` n `8`; equity avg `0.1244` n `108`; fx avg `0.0654` n `6`; index avg `0.0149` n `25`; metal avg `0.3044` n `20`; unknown avg `0.0705` n `749`
- 24h: commodity avg `-1.1693` n `12`; crypto_alt avg `0.8552` n `230`; crypto_major avg `0.8336` n `8`; equity avg `3.2128` n `108`; fx avg `-0.0108` n `6`; index avg `0.698` n `25`; metal avg `1.2481` n `20`; unknown avg `0.1349` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
