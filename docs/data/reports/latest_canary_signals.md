# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T02:22:31.883274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0272` n `12`; crypto_alt avg `0.3666` n `231`; crypto_major avg `0.297` n `8`; equity avg `0.3453` n `122`; fx avg `-0.0028` n `6`; index avg `0.0582` n `25`; metal avg `0.0019` n `20`; unknown avg `0.1558` n `797`
- 1h: commodity avg `0.0022` n `12`; crypto_alt avg `0.344` n `231`; crypto_major avg `0.2113` n `8`; equity avg `0.1975` n `122`; fx avg `-0.0597` n `6`; index avg `0.0652` n `25`; metal avg `0.1345` n `20`; unknown avg `0.1123` n `796`
- 4h: commodity avg `-0.084` n `12`; crypto_alt avg `0.5815` n `231`; crypto_major avg `0.2671` n `8`; equity avg `-0.3459` n `122`; fx avg `-0.0438` n `6`; index avg `-0.0609` n `25`; metal avg `0.1035` n `20`; unknown avg `0.1151` n `795`
- 24h: commodity avg `-0.9291` n `12`; crypto_alt avg `-2.578` n `231`; crypto_major avg `-2.5644` n `8`; equity avg `1.3708` n `122`; fx avg `-0.0163` n `6`; index avg `0.189` n `25`; metal avg `0.1625` n `20`; unknown avg `-0.3497` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
