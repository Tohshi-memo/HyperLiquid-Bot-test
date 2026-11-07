# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T18:22:28.231790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `13`; crypto_alt avg `0.0833` n `239`; crypto_major avg `0.1297` n `8`; equity avg `0.1277` n `158`; fx avg `-0.0018` n `6`; index avg `0.0138` n `27`; metal avg `0.0045` n `20`; unknown avg `0.0081` n `1260`
- 1h: commodity avg `-0.0354` n `13`; crypto_alt avg `0.2839` n `239`; crypto_major avg `0.241` n `8`; equity avg `0.2036` n `158`; fx avg `-0.0115` n `6`; index avg `0.0091` n `27`; metal avg `0.0052` n `20`; unknown avg `0.6114` n `1224`
- 4h: commodity avg `0.0106` n `13`; crypto_alt avg `0.0724` n `239`; crypto_major avg `-0.0819` n `8`; equity avg `0.0689` n `158`; fx avg `-0.0141` n `6`; index avg `0.0303` n `27`; metal avg `-0.0202` n `20`; unknown avg `165.5978` n `1209`
- 24h: commodity avg `0.1547` n `13`; crypto_alt avg `-1.1862` n `239`; crypto_major avg `-0.3761` n `8`; equity avg `1.0008` n `158`; fx avg `0.0029` n `6`; index avg `0.1042` n `27`; metal avg `0.0308` n `20`; unknown avg `0.1395` n `1077`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
