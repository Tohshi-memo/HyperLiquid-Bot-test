# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T18:52:27.196880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0503` n `13`; crypto_alt avg `0.137` n `239`; crypto_major avg `0.2174` n `8`; equity avg `0.058` n `168`; fx avg `-0.0047` n `6`; index avg `0.0019` n `27`; metal avg `0.0075` n `20`; unknown avg `0.1755` n `1262`
- 1h: commodity avg `-0.0179` n `13`; crypto_alt avg `0.2792` n `239`; crypto_major avg `0.4427` n `8`; equity avg `0.5658` n `168`; fx avg `-0.0081` n `6`; index avg `0.0586` n `27`; metal avg `0.0836` n `20`; unknown avg `6.9282` n `1244`
- 4h: commodity avg `-0.3136` n `13`; crypto_alt avg `0.5019` n `239`; crypto_major avg `0.6445` n `8`; equity avg `1.9348` n `168`; fx avg `-0.0746` n `6`; index avg `0.2148` n `27`; metal avg `-0.0502` n `20`; unknown avg `6.9829` n `1230`
- 24h: commodity avg `-0.5927` n `13`; crypto_alt avg `-0.0225` n `239`; crypto_major avg `0.3013` n `8`; equity avg `3.3038` n `168`; fx avg `-0.1628` n `6`; index avg `0.3203` n `27`; metal avg `0.8051` n `20`; unknown avg `75.0911` n `1045`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.13`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1026`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0941`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0839`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0802`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0777`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0607`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0557`, n `669`, weak_sample_signal
