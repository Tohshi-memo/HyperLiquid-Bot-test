# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T08:22:28.997461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.1037` n `230`; crypto_major avg `-0.1887` n `8`; equity avg `0.0196` n `107`; fx avg `0.0034` n `6`; index avg `0.002` n `25`; metal avg `-0.0442` n `20`; unknown avg `-0.0499` n `781`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `0.3359` n `230`; crypto_major avg `0.1902` n `8`; equity avg `0.3873` n `107`; fx avg `0.0298` n `6`; index avg `0.0418` n `25`; metal avg `0.022` n `20`; unknown avg `0.1762` n `781`
- 4h: commodity avg `-0.0507` n `12`; crypto_alt avg `-0.2131` n `230`; crypto_major avg `-0.1913` n `8`; equity avg `1.1919` n `107`; fx avg `0.0509` n `6`; index avg `0.1708` n `25`; metal avg `0.1235` n `20`; unknown avg `0.9033` n `765`
- 24h: commodity avg `0.1494` n `12`; crypto_alt avg `1.4728` n `230`; crypto_major avg `1.673` n `8`; equity avg `3.8142` n `107`; fx avg `0.0937` n `6`; index avg `0.3958` n `25`; metal avg `0.2022` n `20`; unknown avg `1.1731` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
