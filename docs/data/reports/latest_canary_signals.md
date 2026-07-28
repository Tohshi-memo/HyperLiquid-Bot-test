# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T04:22:27.440126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0156` n `12`; crypto_alt avg `-0.0149` n `230`; crypto_major avg `-0.0215` n `8`; equity avg `-0.1154` n `102`; fx avg `-0.0033` n `6`; index avg `-0.0456` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.0825` n `774`
- 1h: commodity avg `0.0699` n `12`; crypto_alt avg `0.0535` n `230`; crypto_major avg `0.0243` n `8`; equity avg `-0.1277` n `102`; fx avg `0.011` n `6`; index avg `-0.0564` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.0651` n `774`
- 4h: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.1625` n `230`; crypto_major avg `-0.2788` n `8`; equity avg `-0.9732` n `102`; fx avg `-0.0651` n `6`; index avg `-0.163` n `25`; metal avg `-0.1768` n `20`; unknown avg `0.2811` n `774`
- 24h: commodity avg `-0.7612` n `12`; crypto_alt avg `-3.9678` n `230`; crypto_major avg `-3.5648` n `8`; equity avg `-3.4219` n `102`; fx avg `-0.1266` n `6`; index avg `-0.7534` n `25`; metal avg `-0.2523` n `20`; unknown avg `1161.8301` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
