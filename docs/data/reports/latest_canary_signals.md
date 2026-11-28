# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T04:07:25.603121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `0.0251` n `239`; crypto_major avg `0.0474` n `8`; equity avg `-0.0281` n `168`; fx avg `-0.0008` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0026` n `20`; unknown avg `0.0515` n `1237`
- 1h: commodity avg `-0.019` n `13`; crypto_alt avg `-0.1263` n `239`; crypto_major avg `0.0636` n `8`; equity avg `-0.0811` n `168`; fx avg `0.0155` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0211` n `20`; unknown avg `0.2968` n `1243`
- 4h: commodity avg `-0.0699` n `13`; crypto_alt avg `-0.6739` n `239`; crypto_major avg `0.1144` n `8`; equity avg `0.065` n `168`; fx avg `0.018` n `6`; index avg `0.0027` n `27`; metal avg `-0.0042` n `20`; unknown avg `255.5181` n `1241`
- 24h: commodity avg `-0.7879` n `13`; crypto_alt avg `-1.4177` n `239`; crypto_major avg `-1.4722` n `8`; equity avg `0.8283` n `168`; fx avg `-0.1413` n `6`; index avg `0.0753` n `27`; metal avg `0.1177` n `20`; unknown avg `214.6813` n `979`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
