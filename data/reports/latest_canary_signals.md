# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T11:52:27.771988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0312` n `13`; crypto_alt avg `-0.1982` n `239`; crypto_major avg `-0.3117` n `8`; equity avg `-0.0775` n `158`; fx avg `-0.0015` n `6`; index avg `-0.0073` n `27`; metal avg `-0.0151` n `20`; unknown avg `0.099` n `1263`
- 1h: commodity avg `-0.4179` n `13`; crypto_alt avg `0.343` n `239`; crypto_major avg `0.1248` n `8`; equity avg `0.1736` n `158`; fx avg `-0.0548` n `6`; index avg `0.0329` n `27`; metal avg `0.0872` n `20`; unknown avg `1.3529` n `1257`
- 4h: commodity avg `-0.3307` n `13`; crypto_alt avg `1.9178` n `239`; crypto_major avg `0.5241` n `8`; equity avg `1.5129` n `158`; fx avg `0.0083` n `6`; index avg `0.1951` n `27`; metal avg `0.2238` n `20`; unknown avg `168.3902` n `1151`
- 24h: commodity avg `-0.6034` n `13`; crypto_alt avg `-1.6563` n `239`; crypto_major avg `-3.7475` n `8`; equity avg `-0.3356` n `158`; fx avg `-0.1459` n `6`; index avg `-0.0003` n `27`; metal avg `0.3371` n `20`; unknown avg `0.8557` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
