# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T20:37:18.847272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0957` n `12`; crypto_alt avg `0.0645` n `228`; crypto_major avg `0.01` n `8`; equity avg `0.0032` n `65`; fx avg `-0.0006` n `5`; index avg `-0.0081` n `23`; metal avg `0.0022` n `18`; unknown avg `0.0676` n `384`
- 1h: commodity avg `-0.1456` n `12`; crypto_alt avg `0.0716` n `228`; crypto_major avg `0.0007` n `8`; equity avg `0.1461` n `65`; fx avg `0.0023` n `5`; index avg `0.0844` n `23`; metal avg `0.0043` n `18`; unknown avg `-0.1056` n `384`
- 4h: commodity avg `-0.0539` n `12`; crypto_alt avg `-0.0367` n `228`; crypto_major avg `0.8341` n `8`; equity avg `0.2621` n `65`; fx avg `0.0133` n `5`; index avg `0.0516` n `23`; metal avg `-0.1105` n `18`; unknown avg `0.135` n `384`
- 24h: commodity avg `1.7338` n `12`; crypto_alt avg `-9.1779` n `228`; crypto_major avg `-1.4906` n `8`; equity avg `-2.2784` n `65`; fx avg `-0.1526` n `5`; index avg `-1.4856` n `23`; metal avg `-5.9423` n `18`; unknown avg `550.4626` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
