# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T12:37:17.816558+00:00`
- Correlation status: `ready`
- Asset price records: `550`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2778` n `12`; crypto_alt avg `0.1516` n `228`; crypto_major avg `0.0497` n `8`; equity avg `-0.0231` n `65`; fx avg `-0.0065` n `5`; index avg `0.0047` n `23`; metal avg `-0.0322` n `18`; unknown avg `0.0142` n `365`
- 1h: commodity avg `-0.4439` n `12`; crypto_alt avg `0.5969` n `228`; crypto_major avg `0.2039` n `8`; equity avg `-0.057` n `65`; fx avg `-0.0115` n `5`; index avg `0.0316` n `23`; metal avg `0.1965` n `18`; unknown avg `0.1541` n `365`
- 4h: commodity avg `-0.9516` n `12`; crypto_alt avg `0.5716` n `228`; crypto_major avg `-0.1074` n `8`; equity avg `0.0191` n `65`; fx avg `0.0313` n `5`; index avg `-0.1466` n `23`; metal avg `0.425` n `18`; unknown avg `0.0791` n `357`
- 24h: commodity avg `-1.5551` n `7`; crypto_alt avg `0.6788` n `223`; crypto_major avg `-2.2691` n `7`; equity avg `0.7031` n `47`; fx avg `0.1044` n `4`; index avg `0.3297` n `6`; metal avg `1.7016` n `7`; unknown avg `0.9819` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1334`, n `546`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `546`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1065`, n `546`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0791`, n `542`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `542`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0753`, n `542`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0743`, n `542`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0709`, n `546`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0662`, n `546`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.065`, n `542`, weak_sample_signal
