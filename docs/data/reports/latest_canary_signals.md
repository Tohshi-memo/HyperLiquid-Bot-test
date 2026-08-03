# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T21:37:27.615432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `0.0385` n `230`; crypto_major avg `-0.0039` n `8`; equity avg `0.0312` n `103`; fx avg `0.0057` n `6`; index avg `0.018` n `25`; metal avg `-0.0089` n `20`; unknown avg `0.0656` n `784`
- 1h: commodity avg `0.037` n `12`; crypto_alt avg `0.0256` n `230`; crypto_major avg `-0.2832` n `8`; equity avg `0.0802` n `103`; fx avg `0.0105` n `6`; index avg `-0.0048` n `25`; metal avg `-0.0134` n `20`; unknown avg `0.1666` n `784`
- 4h: commodity avg `0.0369` n `12`; crypto_alt avg `0.1642` n `230`; crypto_major avg `-0.2206` n `8`; equity avg `0.4617` n `103`; fx avg `0.0189` n `6`; index avg `0.0786` n `25`; metal avg `0.1775` n `20`; unknown avg `-0.0671` n `784`
- 24h: commodity avg `-0.1516` n `12`; crypto_alt avg `0.3003` n `230`; crypto_major avg `0.1293` n `8`; equity avg `1.935` n `103`; fx avg `-0.3012` n `6`; index avg `0.061` n `25`; metal avg `-0.404` n `20`; unknown avg `0.0138` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
