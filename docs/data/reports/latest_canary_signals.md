# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T15:37:31.507948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0365` n `12`; crypto_alt avg `-0.2395` n `230`; crypto_major avg `-0.3088` n `8`; equity avg `-0.1367` n `92`; fx avg `-0.011` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.0408` n `766`
- 1h: commodity avg `0.0537` n `12`; crypto_alt avg `0.0067` n `230`; crypto_major avg `0.0956` n `8`; equity avg `0.0251` n `92`; fx avg `-0.0262` n `6`; index avg `-0.0066` n `25`; metal avg `0.1111` n `20`; unknown avg `-0.0894` n `766`
- 4h: commodity avg `0.1573` n `12`; crypto_alt avg `-0.1632` n `230`; crypto_major avg `-0.4309` n `8`; equity avg `-0.2618` n `92`; fx avg `-0.0259` n `6`; index avg `0.0269` n `25`; metal avg `-0.189` n `20`; unknown avg `-0.0336` n `766`
- 24h: commodity avg `0.086` n `12`; crypto_alt avg `-1.3945` n `230`; crypto_major avg `-2.2467` n `8`; equity avg `-2.1153` n `92`; fx avg `-0.0967` n `6`; index avg `-0.4248` n `25`; metal avg `-0.3501` n `20`; unknown avg `-0.1197` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
