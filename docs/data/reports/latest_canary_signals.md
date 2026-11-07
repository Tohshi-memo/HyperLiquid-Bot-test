# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T00:07:25.006345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `13`; crypto_alt avg `0.0053` n `239`; crypto_major avg `-0.0425` n `8`; equity avg `0.0389` n `158`; fx avg `-0.0153` n `6`; index avg `-0.0018` n `27`; metal avg `0.0098` n `20`; unknown avg `0.6259` n `1251`
- 1h: commodity avg `-0.0069` n `13`; crypto_alt avg `0.105` n `239`; crypto_major avg `0.1234` n `8`; equity avg `0.0193` n `158`; fx avg `-0.0093` n `6`; index avg `0.0071` n `27`; metal avg `-0.003` n `20`; unknown avg `0.2145` n `1247`
- 4h: commodity avg `-0.0656` n `13`; crypto_alt avg `-0.5964` n `239`; crypto_major avg `-0.1845` n `8`; equity avg `-0.0714` n `158`; fx avg `0.0041` n `6`; index avg `-0.0479` n `27`; metal avg `0.0289` n `20`; unknown avg `0.6231` n `1173`
- 24h: commodity avg `0.1156` n `13`; crypto_alt avg `1.7802` n `239`; crypto_major avg `0.1644` n `8`; equity avg `2.861` n `158`; fx avg `-0.0809` n `6`; index avg `0.3593` n `27`; metal avg `-0.0198` n `20`; unknown avg `8.524` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
