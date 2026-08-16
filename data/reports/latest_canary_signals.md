# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T18:22:26.222358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.0373` n `230`; crypto_major avg `-0.0213` n `8`; equity avg `0.006` n `114`; fx avg `-0.0097` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0072` n `20`; unknown avg `-0.0439` n `791`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `-0.2072` n `230`; crypto_major avg `-0.2416` n `8`; equity avg `0.0016` n `114`; fx avg `-0.011` n `6`; index avg `-0.0102` n `25`; metal avg `-0.0034` n `20`; unknown avg `0.0662` n `791`
- 4h: commodity avg `0.0333` n `12`; crypto_alt avg `-0.251` n `230`; crypto_major avg `0.0132` n `8`; equity avg `0.0988` n `114`; fx avg `0.0132` n `6`; index avg `-0.0113` n `25`; metal avg `0.0135` n `20`; unknown avg `-0.0363` n `791`
- 24h: commodity avg `0.0463` n `12`; crypto_alt avg `-0.3054` n `230`; crypto_major avg `0.0291` n `8`; equity avg `0.3216` n `114`; fx avg `-0.0124` n `6`; index avg `0.0117` n `25`; metal avg `0.0439` n `20`; unknown avg `0.1204` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2149`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
