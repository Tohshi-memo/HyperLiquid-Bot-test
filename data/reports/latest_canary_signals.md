# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T10:22:20.611178+00:00`
- Correlation status: `ready`
- Asset price records: `541`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0949` n `12`; crypto_alt avg `-0.1636` n `228`; crypto_major avg `-0.115` n `8`; equity avg `0.0178` n `65`; fx avg `0.0286` n `4`; index avg `0.0283` n `23`; metal avg `-0.0317` n `18`; unknown avg `0.0104` n `366`
- 1h: commodity avg `0.0857` n `12`; crypto_alt avg `-0.2791` n `228`; crypto_major avg `-0.1706` n `8`; equity avg `-0.0551` n `65`; fx avg `0.0109` n `4`; index avg `-0.1276` n `23`; metal avg `0.0972` n `18`; unknown avg `0.0141` n `358`
- 4h: commodity avg `-0.8105` n `12`; crypto_alt avg `0.7353` n `228`; crypto_major avg `0.24` n `8`; equity avg `0.3526` n `65`; fx avg `-0.003` n `4`; index avg `-0.0222` n `23`; metal avg `0.8784` n `18`; unknown avg `0.3552` n `358`
- 24h: commodity avg `-0.5571` n `7`; crypto_alt avg `-0.1927` n `223`; crypto_major avg `-2.1453` n `7`; equity avg `0.3217` n `47`; fx avg `0.1242` n `4`; index avg `0.4652` n `6`; metal avg `1.1301` n `7`; unknown avg `0.7786` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1312`, n `537`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1238`, n `537`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0983`, n `537`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.089`, n `533`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0817`, n `533`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0815`, n `533`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.079`, n `533`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0777`, n `533`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0697`, n `533`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `537`, weak_sample_signal
