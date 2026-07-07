# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T09:52:26.762643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0387` n `12`; crypto_alt avg `0.1239` n `229`; crypto_major avg `0.161` n `8`; equity avg `-0.0018` n `91`; fx avg `-0.0102` n `6`; index avg `0.0054` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0011` n `761`
- 1h: commodity avg `-0.0941` n `12`; crypto_alt avg `0.2266` n `229`; crypto_major avg `0.2839` n `8`; equity avg `-0.2109` n `91`; fx avg `-0.0318` n `6`; index avg `0.0013` n `25`; metal avg `0.0658` n `20`; unknown avg `0.0779` n `757`
- 4h: commodity avg `0.1207` n `12`; crypto_alt avg `0.1075` n `229`; crypto_major avg `0.2409` n `8`; equity avg `-0.2018` n `91`; fx avg `-0.0594` n `6`; index avg `0.0097` n `25`; metal avg `0.2815` n `20`; unknown avg `-0.2536` n `741`
- 24h: commodity avg `0.3525` n `12`; crypto_alt avg `0.7395` n `229`; crypto_major avg `0.3376` n `8`; equity avg `-1.5524` n `90`; fx avg `-0.0913` n `6`; index avg `-0.3492` n `25`; metal avg `-0.1915` n `20`; unknown avg `-0.4018` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
