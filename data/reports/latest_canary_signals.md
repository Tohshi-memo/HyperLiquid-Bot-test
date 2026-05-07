# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T13:07:21.703752+00:00`
- Correlation status: `ready`
- Asset price records: `552`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4515` n `12`; crypto_alt avg `-0.0035` n `228`; crypto_major avg `-0.1688` n `8`; equity avg `-0.0179` n `65`; fx avg `0.0279` n `5`; index avg `-0.0544` n `23`; metal avg `-0.1808` n `18`; unknown avg `0.8826` n `365`
- 1h: commodity avg `-0.2713` n `12`; crypto_alt avg `0.3736` n `228`; crypto_major avg `0.0039` n `8`; equity avg `-0.0531` n `65`; fx avg `0.0105` n `5`; index avg `-0.1456` n `23`; metal avg `0.1066` n `18`; unknown avg `1.0731` n `365`
- 4h: commodity avg `-0.6492` n `12`; crypto_alt avg `0.631` n `228`; crypto_major avg `-0.0642` n `8`; equity avg `0.161` n `65`; fx avg `-0.0054` n `5`; index avg `-0.1694` n `23`; metal avg `0.5346` n `18`; unknown avg `1.7471` n `357`
- 24h: commodity avg `-1.5948` n `7`; crypto_alt avg `1.1637` n `223`; crypto_major avg `-1.6298` n `7`; equity avg `0.9875` n `47`; fx avg `0.0643` n `4`; index avg `0.5348` n `6`; metal avg `1.8915` n `7`; unknown avg `0.9634` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1336`, n `548`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1254`, n `548`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1114`, n `548`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `544`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.076`, n `544`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0751`, n `548`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0748`, n `544`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0744`, n `544`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0697`, n `544`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0638`, n `548`, weak_sample_signal
