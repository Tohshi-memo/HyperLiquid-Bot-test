# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T05:07:27.081755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0299` n `13`; crypto_alt avg `0.208` n `237`; crypto_major avg `0.1472` n `8`; equity avg `0.1156` n `154`; fx avg `-0.0023` n `6`; index avg `0.0244` n `27`; metal avg `-0.0359` n `20`; unknown avg `0.7966` n `1236`
- 1h: commodity avg `-0.0313` n `13`; crypto_alt avg `0.2625` n `237`; crypto_major avg `0.0322` n `8`; equity avg `-0.0214` n `154`; fx avg `-0.0221` n `6`; index avg `0.0678` n `27`; metal avg `-0.1013` n `20`; unknown avg `0.8333` n `1232`
- 4h: commodity avg `-0.039` n `13`; crypto_alt avg `-0.6703` n `237`; crypto_major avg `-0.7071` n `8`; equity avg `-1.0179` n `154`; fx avg `-0.0073` n `6`; index avg `0.0222` n `27`; metal avg `-0.0786` n `20`; unknown avg `207.1584` n `1216`
- 24h: commodity avg `0.0308` n `13`; crypto_alt avg `-0.2108` n `237`; crypto_major avg `0.1516` n `8`; equity avg `0.787` n `153`; fx avg `-0.022` n `6`; index avg `0.1025` n `27`; metal avg `-0.2281` n `20`; unknown avg `1113.6466` n `992`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
