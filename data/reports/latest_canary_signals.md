# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T19:07:27.656289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0394` n `12`; crypto_alt avg `-0.1362` n `230`; crypto_major avg `-0.109` n `8`; equity avg `-0.1575` n `114`; fx avg `-0.0067` n `6`; index avg `-0.0119` n `25`; metal avg `-0.0146` n `20`; unknown avg `-0.1176` n `791`
- 1h: commodity avg `-0.0249` n `12`; crypto_alt avg `-0.3619` n `230`; crypto_major avg `-0.229` n `8`; equity avg `-0.2016` n `114`; fx avg `0.0032` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0244` n `20`; unknown avg `7.6063` n `791`
- 4h: commodity avg `-0.0525` n `12`; crypto_alt avg `0.5075` n `230`; crypto_major avg `-0.0678` n `8`; equity avg `-0.4398` n `114`; fx avg `0.0374` n `6`; index avg `-0.0615` n `25`; metal avg `-0.0797` n `20`; unknown avg `18.851` n `791`
- 24h: commodity avg `0.2225` n `12`; crypto_alt avg `-0.0125` n `230`; crypto_major avg `-1.289` n `8`; equity avg `-0.9965` n `114`; fx avg `0.0767` n `6`; index avg `-0.1284` n `25`; metal avg `0.1362` n `20`; unknown avg `0.0179` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
