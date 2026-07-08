# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T05:37:29.779953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0592` n `12`; crypto_alt avg `-0.0019` n `229`; crypto_major avg `-0.0949` n `8`; equity avg `-0.1698` n `91`; fx avg `-0.02` n `6`; index avg `-0.0581` n `25`; metal avg `0.0776` n `20`; unknown avg `-0.248` n `763`
- 1h: commodity avg `0.1025` n `12`; crypto_alt avg `0.2104` n `229`; crypto_major avg `0.0149` n `8`; equity avg `-0.1064` n `91`; fx avg `-0.0424` n `6`; index avg `-0.0451` n `25`; metal avg `0.0765` n `20`; unknown avg `-0.3571` n `763`
- 4h: commodity avg `0.1651` n `12`; crypto_alt avg `0.0775` n `229`; crypto_major avg `-0.2326` n `8`; equity avg `-0.2241` n `91`; fx avg `-0.0822` n `6`; index avg `-0.2411` n `25`; metal avg `0.3946` n `20`; unknown avg `-0.1132` n `763`
- 24h: commodity avg `0.9679` n `12`; crypto_alt avg `-2.3409` n `229`; crypto_major avg `-1.9278` n `8`; equity avg `-1.4676` n `91`; fx avg `-0.2275` n `6`; index avg `-0.2864` n `25`; metal avg `0.2185` n `20`; unknown avg `-0.2365` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
