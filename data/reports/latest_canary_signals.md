# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T19:22:27.285282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.47` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `0.135` n `230`; crypto_major avg `0.2202` n `8`; equity avg `0.2016` n `92`; fx avg `0.0023` n `6`; index avg `0.0197` n `25`; metal avg `0.0283` n `20`; unknown avg `-0.1261` n `768`
- 1h: commodity avg `0.1192` n `12`; crypto_alt avg `0.1628` n `230`; crypto_major avg `0.4446` n `8`; equity avg `-0.0211` n `92`; fx avg `0.0036` n `6`; index avg `-0.0466` n `25`; metal avg `-0.0141` n `20`; unknown avg `-0.2084` n `768`
- 4h: commodity avg `0.2121` n `12`; crypto_alt avg `-0.2163` n `230`; crypto_major avg `0.3482` n `8`; equity avg `0.0224` n `92`; fx avg `-0.0119` n `6`; index avg `-0.0438` n `25`; metal avg `-0.2813` n `20`; unknown avg `-0.337` n `766`
- 24h: commodity avg `0.3515` n `12`; crypto_alt avg `2.0044` n `230`; crypto_major avg `3.7164` n `8`; equity avg `1.4928` n `92`; fx avg `-0.0082` n `6`; index avg `0.3634` n `25`; metal avg `0.6374` n `20`; unknown avg `0.0263` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
