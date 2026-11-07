# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T14:07:24.313640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `-0.022` n `239`; crypto_major avg `0.0504` n `8`; equity avg `0.0024` n `158`; fx avg `-0.008` n `6`; index avg `-0.0004` n `27`; metal avg `0.0045` n `20`; unknown avg `0.1226` n `1257`
- 1h: commodity avg `0.0363` n `13`; crypto_alt avg `0.1102` n `239`; crypto_major avg `0.237` n `8`; equity avg `-0.0345` n `158`; fx avg `-0.0263` n `6`; index avg `0.0108` n `27`; metal avg `0.0053` n `20`; unknown avg `0.1696` n `1255`
- 4h: commodity avg `0.0133` n `13`; crypto_alt avg `-0.1367` n `239`; crypto_major avg `-0.1883` n `8`; equity avg `0.0485` n `158`; fx avg `0.0267` n `6`; index avg `0.0199` n `27`; metal avg `0.0075` n `20`; unknown avg `-0.0278` n `1249`
- 24h: commodity avg `0.0333` n `13`; crypto_alt avg `-0.9477` n `239`; crypto_major avg `-0.0535` n `8`; equity avg `-0.154` n `158`; fx avg `0.0292` n `6`; index avg `0.0351` n `27`; metal avg `0.259` n `20`; unknown avg `-0.2426` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
