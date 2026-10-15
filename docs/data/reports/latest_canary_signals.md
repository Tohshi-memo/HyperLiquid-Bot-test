# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T14:37:33.032203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0517` n `13`; crypto_alt avg `0.2977` n `236`; crypto_major avg `0.212` n `8`; equity avg `0.0202` n `151`; fx avg `0.008` n `6`; index avg `-0.0085` n `26`; metal avg `0.0505` n `20`; unknown avg `1.4311` n `1136`
- 1h: commodity avg `0.1474` n `13`; crypto_alt avg `1.4256` n `236`; crypto_major avg `1.0844` n `8`; equity avg `0.6539` n `151`; fx avg `0.0451` n `6`; index avg `0.0996` n `26`; metal avg `-0.0513` n `20`; unknown avg `2.3843` n `1092`
- 4h: commodity avg `0.1518` n `13`; crypto_alt avg `0.7496` n `236`; crypto_major avg `0.1925` n `8`; equity avg `-0.2916` n `151`; fx avg `0.0499` n `6`; index avg `0.0535` n `26`; metal avg `0.018` n `20`; unknown avg `1.537` n `1086`
- 24h: commodity avg `-0.0024` n `13`; crypto_alt avg `-1.6339` n `236`; crypto_major avg `-1.1025` n `8`; equity avg `-4.3002` n `151`; fx avg `0.2066` n `6`; index avg `-0.64` n `26`; metal avg `0.1623` n `20`; unknown avg `-1.0014` n `941`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0809`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0767`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0709`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0701`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
