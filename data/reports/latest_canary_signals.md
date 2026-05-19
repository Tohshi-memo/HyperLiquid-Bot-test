# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T09:37:20.763192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `-0.1499` n `228`; crypto_major avg `-0.2661` n `8`; equity avg `-0.2836` n `66`; fx avg `-0.0052` n `6`; index avg `-0.1198` n `23`; metal avg `-0.1076` n `18`; unknown avg `0.8431` n `383`
- 1h: commodity avg `0.0738` n `12`; crypto_alt avg `-0.6507` n `228`; crypto_major avg `-0.4984` n `8`; equity avg `-0.548` n `66`; fx avg `-0.0587` n `6`; index avg `-0.2839` n `23`; metal avg `-0.2025` n `18`; unknown avg `0.5922` n `383`
- 4h: commodity avg `0.2038` n `12`; crypto_alt avg `-0.6737` n `228`; crypto_major avg `-0.4002` n `8`; equity avg `-0.342` n `66`; fx avg `-0.0767` n `6`; index avg `-0.2667` n `23`; metal avg `-0.1813` n `18`; unknown avg `0.6761` n `363`
- 24h: commodity avg `0.7236` n `12`; crypto_alt avg `1.0474` n `228`; crypto_major avg `0.4991` n `8`; equity avg `-1.9499` n `66`; fx avg `0.2261` n `6`; index avg `-0.9056` n `23`; metal avg `-0.2648` n `18`; unknown avg `1.6008` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
