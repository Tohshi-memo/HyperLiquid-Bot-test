# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T19:15:21.140586+00:00`
- Correlation status: `ready`
- Asset price records: `291`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1382` n `7`; crypto_alt avg `-0.1421` n `223`; crypto_major avg `-0.0626` n `7`; equity avg `-0.0339` n `42`; fx avg `0.0104` n `4`; index avg `0.1429` n `9`; metal avg `0.0797` n `7`; unknown avg `-0.1373` n `314`
- 1h: commodity avg `-0.0494` n `7`; crypto_alt avg `-0.1243` n `223`; crypto_major avg `-0.2497` n `7`; equity avg `-0.0179` n `42`; fx avg `-0.0134` n `4`; index avg `0.1118` n `9`; metal avg `0.0283` n `7`; unknown avg `-0.2719` n `314`
- 4h: commodity avg `0.3011` n `7`; crypto_alt avg `0.0864` n `223`; crypto_major avg `-0.3152` n `7`; equity avg `-1.2556` n `42`; fx avg `-0.0254` n `4`; index avg `-0.3671` n `9`; metal avg `-0.5419` n `7`; unknown avg `-0.3723` n `314`
- 24h: commodity avg `1.5525` n `7`; crypto_alt avg `1.892` n `223`; crypto_major avg `1.1514` n `7`; equity avg `-0.286` n `42`; fx avg `-0.0647` n `4`; index avg `0.6353` n `9`; metal avg `-2.3072` n `7`; unknown avg `-1.0657` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2377`, n `287`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2321`, n `287`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.166`, n `283`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.165`, n `283`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1496`, n `287`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1482`, n `287`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.143`, n `287`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1313`, n `283`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1312`, n `283`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1286`, n `287`, weak_sample_signal
