# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T10:52:21.108359+00:00`
- Correlation status: `ready`
- Asset price records: `543`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1438` n `12`; crypto_alt avg `0.2949` n `228`; crypto_major avg `0.1587` n `8`; equity avg `0.0938` n `65`; fx avg `0.0069` n `4`; index avg `0.0663` n `23`; metal avg `0.0932` n `18`; unknown avg `0.122` n `366`
- 1h: commodity avg `0.1074` n `12`; crypto_alt avg `0.0809` n `228`; crypto_major avg `-0.1136` n `8`; equity avg `-0.2421` n `65`; fx avg `0.0121` n `4`; index avg `0.0504` n `23`; metal avg `-0.0171` n `18`; unknown avg `-0.1441` n `358`
- 4h: commodity avg `-0.4011` n `12`; crypto_alt avg `0.1002` n `228`; crypto_major avg `-0.34` n `8`; equity avg `0.0941` n `65`; fx avg `0.082` n `4`; index avg `-0.0565` n `23`; metal avg `0.5473` n `18`; unknown avg `0.2559` n `358`
- 24h: commodity avg `0.2685` n `7`; crypto_alt avg `-0.1946` n `223`; crypto_major avg `-2.3036` n `7`; equity avg `0.2139` n `47`; fx avg `0.2354` n `4`; index avg `0.352` n `6`; metal avg `0.8974` n `7`; unknown avg `0.838` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1308`, n `539`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1232`, n `539`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0941`, n `539`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0831`, n `535`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0791`, n `535`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `535`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0766`, n `535`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `539`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.071`, n `535`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `535`, weak_sample_signal
