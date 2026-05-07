# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T04:22:19.290123+00:00`
- Correlation status: `ready`
- Asset price records: `517`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `0.5215` n `228`; crypto_major avg `0.2384` n `8`; equity avg `0.099` n `65`; fx avg `-0.0412` n `4`; index avg `0.0008` n `23`; metal avg `-0.0317` n `18`; unknown avg `0.1383` n `358`
- 1h: commodity avg `0.0003` n `12`; crypto_alt avg `0.3567` n `228`; crypto_major avg `0.2257` n `8`; equity avg `0.2519` n `65`; fx avg `-0.0103` n `4`; index avg `0.0004` n `23`; metal avg `-0.2213` n `18`; unknown avg `0.0153` n `358`
- 4h: commodity avg `-0.1945` n `12`; crypto_alt avg `-0.6081` n `228`; crypto_major avg `-0.7686` n `8`; equity avg `0.3295` n `65`; fx avg `0.0668` n `4`; index avg `0.141` n `23`; metal avg `0.0161` n `18`; unknown avg `-0.4028` n `356`
- 24h: commodity avg `-1.7644` n `7`; crypto_alt avg `0.1534` n `223`; crypto_major avg `-1.3717` n `7`; equity avg `1.3288` n `47`; fx avg `-0.2404` n `4`; index avg `1.0899` n `6`; metal avg `1.4305` n `7`; unknown avg `1.427` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `513`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1098`, n `513`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `513`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `513`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0836`, n `509`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0764`, n `509`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0728`, n `509`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0717`, n `509`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0696`, n `509`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `513`, weak_sample_signal
