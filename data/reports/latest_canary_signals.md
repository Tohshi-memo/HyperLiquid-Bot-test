# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T05:22:34.513580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `13`; crypto_alt avg `-0.1844` n `237`; crypto_major avg `-0.1042` n `8`; equity avg `-0.2036` n `154`; fx avg `-0.0044` n `6`; index avg `-0.0548` n `27`; metal avg `-0.0401` n `20`; unknown avg `0.6247` n `1238`
- 1h: commodity avg `-0.0002` n `13`; crypto_alt avg `0.0178` n `237`; crypto_major avg `-0.1054` n `8`; equity avg `-0.2094` n `154`; fx avg `-0.0205` n `6`; index avg `0.0697` n `27`; metal avg `-0.1659` n `20`; unknown avg `1.9299` n `1232`
- 4h: commodity avg `-0.0528` n `13`; crypto_alt avg `-0.4709` n `237`; crypto_major avg `-0.4854` n `8`; equity avg `-0.992` n `154`; fx avg `-0.0249` n `6`; index avg `-0.0105` n `27`; metal avg `-0.0977` n `20`; unknown avg `292.3601` n `1216`
- 24h: commodity avg `0.0152` n `13`; crypto_alt avg `-0.4555` n `237`; crypto_major avg `-0.0525` n `8`; equity avg `0.5297` n `153`; fx avg `-0.0386` n `6`; index avg `0.0447` n `27`; metal avg `-0.2459` n `20`; unknown avg `1112.7429` n `992`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
