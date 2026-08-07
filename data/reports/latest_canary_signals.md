# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T05:52:26.666440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.2973` n `230`; crypto_major avg `0.2171` n `8`; equity avg `0.0321` n `112`; fx avg `-0.0057` n `6`; index avg `-0.0012` n `25`; metal avg `0.0367` n `20`; unknown avg `0.0531` n `782`
- 1h: commodity avg `-0.0062` n `12`; crypto_alt avg `0.5508` n `230`; crypto_major avg `0.1326` n `8`; equity avg `0.4054` n `112`; fx avg `-0.0037` n `6`; index avg `0.0524` n `25`; metal avg `0.1348` n `20`; unknown avg `-0.1815` n `782`
- 4h: commodity avg `0.1288` n `12`; crypto_alt avg `-0.0351` n `230`; crypto_major avg `-0.4568` n `8`; equity avg `0.6934` n `112`; fx avg `0.0097` n `6`; index avg `0.0844` n `25`; metal avg `0.1791` n `20`; unknown avg `-0.4983` n `782`
- 24h: commodity avg `0.725` n `12`; crypto_alt avg `0.4292` n `230`; crypto_major avg `-1.347` n `8`; equity avg `1.0258` n `109`; fx avg `0.0262` n `6`; index avg `-0.0669` n `25`; metal avg `0.0603` n `20`; unknown avg `113.1712` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
