# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T02:22:27.428704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.036` n `12`; crypto_alt avg `-0.0844` n `230`; crypto_major avg `-0.0336` n `8`; equity avg `-0.3815` n `114`; fx avg `0.0005` n `6`; index avg `-0.0639` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.0029` n `793`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `-0.4022` n `230`; crypto_major avg `-0.3196` n `8`; equity avg `-1.2961` n `114`; fx avg `0.0116` n `6`; index avg `-0.1656` n `25`; metal avg `-0.2034` n `20`; unknown avg `0.5773` n `793`
- 4h: commodity avg `-0.0379` n `12`; crypto_alt avg `-0.5272` n `230`; crypto_major avg `-0.2141` n `8`; equity avg `-1.3156` n `114`; fx avg `-0.0671` n `6`; index avg `-0.1916` n `25`; metal avg `-0.1447` n `20`; unknown avg `-0.1066` n `793`
- 24h: commodity avg `0.502` n `12`; crypto_alt avg `-0.436` n `230`; crypto_major avg `0.4924` n `8`; equity avg `-0.4171` n `114`; fx avg `0.0122` n `6`; index avg `-0.1441` n `25`; metal avg `-0.1466` n `20`; unknown avg `0.2081` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
