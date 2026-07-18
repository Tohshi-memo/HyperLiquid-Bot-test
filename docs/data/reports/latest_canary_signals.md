# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T01:52:23.813653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `-0.0291` n `230`; crypto_major avg `0.068` n `8`; equity avg `-0.0161` n `96`; fx avg `-0.0078` n `6`; index avg `0.0193` n `25`; metal avg `-0.0033` n `20`; unknown avg `-0.2174` n `769`
- 1h: commodity avg `0.0124` n `12`; crypto_alt avg `-0.102` n `230`; crypto_major avg `0.0271` n `8`; equity avg `0.0872` n `96`; fx avg `-0.004` n `6`; index avg `0.015` n `25`; metal avg `-0.0004` n `20`; unknown avg `-0.2847` n `769`
- 4h: commodity avg `-0.0253` n `12`; crypto_alt avg `0.133` n `230`; crypto_major avg `-0.0458` n `8`; equity avg `0.1821` n `96`; fx avg `-0.003` n `6`; index avg `0.0225` n `25`; metal avg `0.0795` n `20`; unknown avg `-0.2866` n `769`
- 24h: commodity avg `0.6597` n `12`; crypto_alt avg `-0.1613` n `230`; crypto_major avg `0.0077` n `8`; equity avg `0.3618` n `94`; fx avg `0.0621` n `6`; index avg `-0.0297` n `25`; metal avg `0.1835` n `20`; unknown avg `0.229` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
