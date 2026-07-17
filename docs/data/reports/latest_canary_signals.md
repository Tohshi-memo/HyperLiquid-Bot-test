# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T07:01:06.718975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0477` n `12`; crypto_alt avg `-0.0508` n `230`; crypto_major avg `0.0693` n `8`; equity avg `-0.0776` n `96`; fx avg `-0.0128` n `6`; index avg `-0.0012` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0013` n `768`
- 1h: commodity avg `0.0919` n `12`; crypto_alt avg `0.1257` n `230`; crypto_major avg `0.1168` n `8`; equity avg `0.0747` n `96`; fx avg `0.0245` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.0616` n `768`
- 4h: commodity avg `-0.1528` n `12`; crypto_alt avg `-0.4784` n `230`; crypto_major avg `-0.8637` n `8`; equity avg `-0.8488` n `94`; fx avg `0.011` n `6`; index avg `-0.1509` n `25`; metal avg `-0.0681` n `20`; unknown avg `-0.1033` n `736`
- 24h: commodity avg `-0.1507` n `12`; crypto_alt avg `-2.2916` n `230`; crypto_major avg `-3.7634` n `8`; equity avg `-5.7523` n `94`; fx avg `-0.0609` n `6`; index avg `-0.7841` n `25`; metal avg `-0.7616` n `20`; unknown avg `-0.6095` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
