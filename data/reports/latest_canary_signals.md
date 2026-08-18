# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T13:07:24.813924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.0619` n `230`; crypto_major avg `-0.1601` n `8`; equity avg `-0.1191` n `114`; fx avg `-0.0001` n `6`; index avg `-0.0115` n `25`; metal avg `-0.0832` n `20`; unknown avg `-0.0035` n `795`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `-0.0525` n `230`; crypto_major avg `-0.3222` n `8`; equity avg `-0.4227` n `114`; fx avg `0.0087` n `6`; index avg `-0.0373` n `25`; metal avg `-0.0408` n `20`; unknown avg `0.042` n `795`
- 4h: commodity avg `0.038` n `12`; crypto_alt avg `0.1585` n `230`; crypto_major avg `-0.1327` n `8`; equity avg `-0.245` n `114`; fx avg `-0.0236` n `6`; index avg `0.0096` n `25`; metal avg `0.0122` n `20`; unknown avg `0.2567` n `795`
- 24h: commodity avg `0.5994` n `12`; crypto_alt avg `-0.6781` n `230`; crypto_major avg `0.0971` n `8`; equity avg `-2.5031` n `114`; fx avg `-0.0535` n `6`; index avg `-0.501` n `25`; metal avg `-0.2109` n `20`; unknown avg `-0.0858` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
