# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T09:37:30.390260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `13`; crypto_alt avg `-0.2133` n `238`; crypto_major avg `-0.1404` n `8`; equity avg `-0.06` n `154`; fx avg `-0.0005` n `6`; index avg `-0.032` n `27`; metal avg `0.0156` n `20`; unknown avg `5.6013` n `1238`
- 1h: commodity avg `-0.0887` n `13`; crypto_alt avg `-0.1841` n `238`; crypto_major avg `-0.1712` n `8`; equity avg `0.2991` n `154`; fx avg `-0.0248` n `6`; index avg `0.0696` n `27`; metal avg `0.0688` n `20`; unknown avg `6.0949` n `1236`
- 4h: commodity avg `0.2558` n `13`; crypto_alt avg `0.0601` n `237`; crypto_major avg `-0.0918` n `8`; equity avg `0.224` n `154`; fx avg `-0.0171` n `6`; index avg `0.0366` n `27`; metal avg `-0.1046` n `20`; unknown avg `-0.3694` n `1174`
- 24h: commodity avg `0.1663` n `13`; crypto_alt avg `-0.7614` n `237`; crypto_major avg `-0.4375` n `8`; equity avg `0.5626` n `153`; fx avg `-0.0644` n `6`; index avg `0.2782` n `27`; metal avg `-0.3748` n `20`; unknown avg `1068.6819` n `1040`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
