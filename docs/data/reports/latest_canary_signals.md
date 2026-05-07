# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T22:52:13.534078+00:00`
- Correlation status: `ready`
- Asset price records: `591`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0394` n `12`; crypto_alt avg `0.1381` n `228`; crypto_major avg `0.0622` n `8`; equity avg `0.08` n `65`; fx avg `-0.0113` n `5`; index avg `-0.025` n `23`; metal avg `-0.1198` n `18`; unknown avg `-0.0677` n `365`
- 1h: commodity avg `-0.2047` n `12`; crypto_alt avg `-0.1125` n `228`; crypto_major avg `-0.2285` n `8`; equity avg `0.1438` n `65`; fx avg `0.0035` n `5`; index avg `0.0865` n `23`; metal avg `-0.0785` n `18`; unknown avg `-0.1729` n `365`
- 4h: commodity avg `0.4431` n `12`; crypto_alt avg `-0.0475` n `228`; crypto_major avg `-0.2686` n `8`; equity avg `-0.349` n `65`; fx avg `-0.0474` n `5`; index avg `0.0518` n `23`; metal avg `-0.3879` n `18`; unknown avg `-0.7714` n `365`
- 24h: commodity avg `0.7888` n `12`; crypto_alt avg `1.1674` n `228`; crypto_major avg `-1.9472` n `8`; equity avg `-1.6547` n `65`; fx avg `0.154` n `5`; index avg `-0.8953` n `23`; metal avg `-0.4836` n `18`; unknown avg `-0.478` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1397`, n `587`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `587`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `587`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `587`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `583`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `583`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0893`, n `583`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0876`, n `583`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.083`, n `583`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `583`, weak_sample_signal
