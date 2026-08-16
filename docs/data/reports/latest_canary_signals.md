# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T17:52:25.021438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `-0.0198` n `230`; crypto_major avg `-0.0707` n `8`; equity avg `0.0087` n `114`; fx avg `0.0093` n `6`; index avg `-0.0081` n `25`; metal avg `0.0043` n `20`; unknown avg `0.1267` n `791`
- 1h: commodity avg `0.0123` n `12`; crypto_alt avg `-0.0648` n `230`; crypto_major avg `-0.0957` n `8`; equity avg `0.0029` n `114`; fx avg `-0.0011` n `6`; index avg `-0.0165` n `25`; metal avg `0.0089` n `20`; unknown avg `0.0548` n `791`
- 4h: commodity avg `0.0268` n `12`; crypto_alt avg `-0.0183` n `230`; crypto_major avg `0.1828` n `8`; equity avg `0.1081` n `114`; fx avg `0.0081` n `6`; index avg `-0.0173` n `25`; metal avg `0.0248` n `20`; unknown avg `-0.0606` n `791`
- 24h: commodity avg `0.0426` n `12`; crypto_alt avg `-0.2988` n `230`; crypto_major avg `0.045` n `8`; equity avg `0.3197` n `114`; fx avg `-0.0081` n `6`; index avg `0.011` n `25`; metal avg `0.0595` n `20`; unknown avg `0.1124` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2147`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
