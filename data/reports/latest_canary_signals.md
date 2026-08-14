# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T18:22:27.544909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0257` n `12`; crypto_alt avg `-0.0176` n `230`; crypto_major avg `0.0415` n `8`; equity avg `-0.0467` n `114`; fx avg `-0.0082` n `6`; index avg `0.0055` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0442` n `791`
- 1h: commodity avg `-0.008` n `12`; crypto_alt avg `-0.1124` n `230`; crypto_major avg `-0.2961` n `8`; equity avg `-0.1277` n `114`; fx avg `-0.0067` n `6`; index avg `0.0051` n `25`; metal avg `-0.0424` n `20`; unknown avg `1.6127` n `791`
- 4h: commodity avg `0.0825` n `12`; crypto_alt avg `0.6991` n `230`; crypto_major avg `0.3123` n `8`; equity avg `-0.4759` n `114`; fx avg `0.0268` n `6`; index avg `-0.0876` n `25`; metal avg `-0.0564` n `20`; unknown avg `37.9336` n `786`
- 24h: commodity avg `0.1985` n `12`; crypto_alt avg `0.5154` n `230`; crypto_major avg `-0.6879` n `8`; equity avg `-0.6233` n `114`; fx avg `0.06` n `6`; index avg `-0.0907` n `25`; metal avg `0.1276` n `20`; unknown avg `0.1036` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
