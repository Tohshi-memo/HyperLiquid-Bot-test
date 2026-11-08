# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T06:22:27.353590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `13`; crypto_alt avg `0.1032` n `239`; crypto_major avg `0.062` n `8`; equity avg `-0.0111` n `158`; fx avg `-0.0021` n `6`; index avg `-0.0018` n `27`; metal avg `-0.0087` n `20`; unknown avg `0.0373` n `1256`
- 1h: commodity avg `-0.0264` n `13`; crypto_alt avg `0.172` n `239`; crypto_major avg `0.0663` n `8`; equity avg `0.0489` n `158`; fx avg `0.0143` n `6`; index avg `0.0032` n `27`; metal avg `-0.0073` n `20`; unknown avg `-0.0225` n `1224`
- 4h: commodity avg `-0.051` n `13`; crypto_alt avg `0.0426` n `239`; crypto_major avg `0.1833` n `8`; equity avg `0.0843` n `158`; fx avg `0.0149` n `6`; index avg `0.0148` n `27`; metal avg `-0.0102` n `20`; unknown avg `-0.1165` n `1210`
- 24h: commodity avg `0.1204` n `13`; crypto_alt avg `-1.5151` n `239`; crypto_major avg `-0.6071` n `8`; equity avg `0.0308` n `158`; fx avg `0.0471` n `6`; index avg `0.0357` n `27`; metal avg `-0.0532` n `20`; unknown avg `158.8802` n `1081`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
