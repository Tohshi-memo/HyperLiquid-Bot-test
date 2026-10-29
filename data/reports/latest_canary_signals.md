# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T08:22:37.997954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0211` n `13`; crypto_alt avg `0.3227` n `238`; crypto_major avg `0.2023` n `8`; equity avg `0.197` n `155`; fx avg `-0.004` n `6`; index avg `0.0288` n `27`; metal avg `-0.0338` n `20`; unknown avg `0.0531` n `1238`
- 1h: commodity avg `-0.0041` n `13`; crypto_alt avg `0.2799` n `238`; crypto_major avg `0.2091` n `8`; equity avg `-0.0237` n `155`; fx avg `0.0111` n `6`; index avg `-0.0366` n `27`; metal avg `-0.034` n `20`; unknown avg `418.3623` n `1216`
- 4h: commodity avg `-0.0181` n `13`; crypto_alt avg `-0.1206` n `238`; crypto_major avg `0.3008` n `8`; equity avg `-0.1055` n `155`; fx avg `0.0044` n `6`; index avg `0.0309` n `27`; metal avg `-0.1153` n `20`; unknown avg `0.1636` n `1180`
- 24h: commodity avg `-0.0988` n `13`; crypto_alt avg `-2.581` n `238`; crypto_major avg `-1.6558` n `8`; equity avg `-1.5175` n `154`; fx avg `0.0344` n `6`; index avg `-0.0805` n `27`; metal avg `-0.3855` n `20`; unknown avg `31.4219` n `968`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
