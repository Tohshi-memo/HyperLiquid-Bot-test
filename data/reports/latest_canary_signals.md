# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T22:07:20.052128+00:00`
- Correlation status: `ready`
- Asset price records: `588`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0536` n `12`; crypto_alt avg `-0.3819` n `228`; crypto_major avg `-0.3472` n `8`; equity avg `0.1064` n `65`; fx avg `0.0078` n `5`; index avg `0.089` n `23`; metal avg `-0.0977` n `18`; unknown avg `-0.0085` n `365`
- 1h: commodity avg `-0.2817` n `12`; crypto_alt avg `0.0733` n `228`; crypto_major avg `-0.163` n `8`; equity avg `-0.525` n `65`; fx avg `0.0065` n `5`; index avg `-0.1319` n `23`; metal avg `-0.1274` n `18`; unknown avg `-0.0405` n `365`
- 4h: commodity avg `1.0593` n `12`; crypto_alt avg `-0.4951` n `228`; crypto_major avg `-0.7586` n `8`; equity avg `-0.8777` n `65`; fx avg `-0.0214` n `5`; index avg `-0.3333` n `23`; metal avg `-0.961` n `18`; unknown avg `-0.5817` n `365`
- 24h: commodity avg `0.9837` n `12`; crypto_alt avg `0.6089` n `228`; crypto_major avg `-2.248` n `8`; equity avg `-1.5049` n `65`; fx avg `0.1592` n `5`; index avg `-0.9049` n `23`; metal avg `-0.4179` n `18`; unknown avg `-0.6172` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1401`, n `584`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `584`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `584`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `584`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `580`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `580`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0922`, n `580`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0884`, n `580`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0824`, n `580`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.079`, n `580`, weak_sample_signal
