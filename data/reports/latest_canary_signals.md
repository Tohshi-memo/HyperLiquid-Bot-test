# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T18:07:30.934347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0221` n `13`; crypto_alt avg `0.0707` n `239`; crypto_major avg `0.0508` n `8`; equity avg `-0.0076` n `158`; fx avg `0.0012` n `6`; index avg `-0.0156` n `27`; metal avg `0.0035` n `20`; unknown avg `0.2642` n `1242`
- 1h: commodity avg `-0.0375` n `13`; crypto_alt avg `0.3353` n `239`; crypto_major avg `0.1699` n `8`; equity avg `0.0937` n `158`; fx avg `-0.0104` n `6`; index avg `0.0048` n `27`; metal avg `0.0024` n `20`; unknown avg `0.8886` n `1224`
- 4h: commodity avg `0.0297` n `13`; crypto_alt avg `-0.058` n `239`; crypto_major avg `-0.2057` n `8`; equity avg `-0.0783` n `158`; fx avg `-0.0193` n `6`; index avg `0.0166` n `27`; metal avg `-0.026` n `20`; unknown avg `165.6093` n `1209`
- 24h: commodity avg `0.2396` n `13`; crypto_alt avg `-1.1887` n `239`; crypto_major avg `-0.462` n `8`; equity avg `0.8411` n `158`; fx avg `0.0102` n `6`; index avg `0.0839` n `27`; metal avg `0.0319` n `20`; unknown avg `0.2477` n `1079`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
