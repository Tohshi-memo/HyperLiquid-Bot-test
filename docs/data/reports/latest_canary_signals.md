# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T02:22:31.433057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.1701` n `230`; crypto_major avg `-0.2234` n `8`; equity avg `0.265` n `108`; fx avg `0.0227` n `6`; index avg `0.043` n `25`; metal avg `-0.0643` n `20`; unknown avg `0.1565` n `782`
- 1h: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.4035` n `230`; crypto_major avg `-0.4515` n `8`; equity avg `0.6703` n `108`; fx avg `-0.0087` n `6`; index avg `0.0597` n `25`; metal avg `0.1695` n `20`; unknown avg `0.1659` n `782`
- 4h: commodity avg `0.0968` n `12`; crypto_alt avg `-0.3346` n `230`; crypto_major avg `-0.6417` n `8`; equity avg `-0.2285` n `108`; fx avg `-0.0612` n `6`; index avg `-0.1684` n `25`; metal avg `0.2969` n `20`; unknown avg `0.0282` n `782`
- 24h: commodity avg `0.0954` n `12`; crypto_alt avg `-0.1319` n `230`; crypto_major avg `-0.3885` n `8`; equity avg `-1.5268` n `108`; fx avg `-0.0142` n `6`; index avg `-0.3265` n `25`; metal avg `0.9695` n `20`; unknown avg `0.9288` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
