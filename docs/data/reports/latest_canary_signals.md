# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T04:37:33.401662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `-0.0014` n `230`; crypto_major avg `0.0442` n `8`; equity avg `-0.0386` n `107`; fx avg `-0.0101` n `6`; index avg `-0.0114` n `25`; metal avg `0.0201` n `20`; unknown avg `3.2785` n `781`
- 1h: commodity avg `0.0554` n `12`; crypto_alt avg `0.0647` n `230`; crypto_major avg `0.117` n `8`; equity avg `0.0169` n `107`; fx avg `0.005` n `6`; index avg `-0.003` n `25`; metal avg `0.0501` n `20`; unknown avg `3.1033` n `781`
- 4h: commodity avg `0.114` n `12`; crypto_alt avg `0.4382` n `230`; crypto_major avg `0.6833` n `8`; equity avg `0.5117` n `107`; fx avg `0.045` n `6`; index avg `0.0458` n `25`; metal avg `0.2128` n `20`; unknown avg `1.2662` n `780`
- 24h: commodity avg `0.3159` n `12`; crypto_alt avg `1.1432` n `230`; crypto_major avg `1.0901` n `8`; equity avg `1.5159` n `107`; fx avg `0.0511` n `6`; index avg `0.0821` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.2494` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
