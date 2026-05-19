# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T11:37:17.247548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1548` n `12`; crypto_alt avg `-0.0119` n `228`; crypto_major avg `-0.0447` n `8`; equity avg `0.026` n `66`; fx avg `0.0093` n `6`; index avg `0.0131` n `23`; metal avg `-0.1126` n `18`; unknown avg `-0.048` n `383`
- 1h: commodity avg `0.4204` n `12`; crypto_alt avg `-0.3854` n `228`; crypto_major avg `-0.3052` n `8`; equity avg `-0.1245` n `66`; fx avg `-0.0227` n `6`; index avg `0.0208` n `23`; metal avg `-0.1344` n `18`; unknown avg `-0.4406` n `383`
- 4h: commodity avg `0.3052` n `12`; crypto_alt avg `-1.123` n `228`; crypto_major avg `-0.6929` n `8`; equity avg `-0.7559` n `66`; fx avg `-0.0712` n `6`; index avg `-0.3787` n `23`; metal avg `-0.1862` n `18`; unknown avg `-0.7864` n `383`
- 24h: commodity avg `1.1228` n `12`; crypto_alt avg `1.0009` n `228`; crypto_major avg `0.6758` n `8`; equity avg `-1.4957` n `66`; fx avg `0.1958` n `6`; index avg `-0.5987` n `23`; metal avg `-0.3855` n `18`; unknown avg `0.6584` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
