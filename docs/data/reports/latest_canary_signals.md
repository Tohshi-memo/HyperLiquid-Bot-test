# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T15:52:35.987353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `13`; crypto_alt avg `0.2661` n `239`; crypto_major avg `0.5263` n `8`; equity avg `1.0728` n `158`; fx avg `0.0018` n `6`; index avg `0.1237` n `27`; metal avg `0.0718` n `20`; unknown avg `1.7389` n `1257`
- 1h: commodity avg `-0.2272` n `13`; crypto_alt avg `-0.2655` n `239`; crypto_major avg `0.1814` n `8`; equity avg `-0.6036` n `158`; fx avg `-0.003` n `6`; index avg `-0.0138` n `27`; metal avg `0.0049` n `20`; unknown avg `1.0824` n `1255`
- 4h: commodity avg `-0.4269` n `13`; crypto_alt avg `0.0232` n `239`; crypto_major avg `-0.2522` n `8`; equity avg `-0.9784` n `158`; fx avg `-0.0085` n `6`; index avg `0.0342` n `27`; metal avg `-0.0438` n `20`; unknown avg `66.0859` n `1229`
- 24h: commodity avg `-0.0315` n `13`; crypto_alt avg `3.4486` n `239`; crypto_major avg `0.0271` n `8`; equity avg `3.59` n `158`; fx avg `-0.1055` n `6`; index avg `0.2218` n `27`; metal avg `-0.0979` n `20`; unknown avg `2.5904` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
