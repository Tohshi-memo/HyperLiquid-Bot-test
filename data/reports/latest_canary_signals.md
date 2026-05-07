# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T09:07:23.009706+00:00`
- Correlation status: `ready`
- Asset price records: `536`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0734` n `12`; crypto_alt avg `-0.1799` n `228`; crypto_major avg `-0.2328` n `8`; equity avg `-0.083` n `65`; fx avg `0.0373` n `4`; index avg `-0.0689` n `23`; metal avg `-0.0664` n `18`; unknown avg `-0.0234` n `358`
- 1h: commodity avg `0.0274` n `12`; crypto_alt avg `-0.2642` n `228`; crypto_major avg `-0.5086` n `8`; equity avg `-0.427` n `65`; fx avg `0.0969` n `4`; index avg `-0.1508` n `23`; metal avg `-0.263` n `18`; unknown avg `0.1054` n `358`
- 4h: commodity avg `-0.8674` n `12`; crypto_alt avg `0.8442` n `228`; crypto_major avg `0.4462` n `8`; equity avg `0.1791` n `65`; fx avg `0.0411` n `4`; index avg `0.1248` n `23`; metal avg `1.0127` n `18`; unknown avg `0.3514` n `356`
- 24h: commodity avg `-0.9988` n `7`; crypto_alt avg `0.2543` n `223`; crypto_major avg `-1.6973` n `7`; equity avg `0.5331` n `47`; fx avg `0.1114` n `4`; index avg `0.691` n `6`; metal avg `1.3243` n `7`; unknown avg `0.9671` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1304`, n `532`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `532`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0952`, n `532`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0759`, n `528`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.075`, n `528`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0723`, n `528`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0708`, n `528`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0692`, n `528`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0684`, n `528`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0677`, n `528`, weak_sample_signal
