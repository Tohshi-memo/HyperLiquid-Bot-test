# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T05:22:26.453629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `-0.0804` n `229`; crypto_major avg `0.1054` n `8`; equity avg `-0.0304` n `88`; fx avg `0.0226` n `6`; index avg `-0.0087` n `25`; metal avg `-0.0746` n `20`; unknown avg `4.1946` n `765`
- 1h: commodity avg `0.04` n `12`; crypto_alt avg `-0.0121` n `229`; crypto_major avg `0.258` n `8`; equity avg `0.0681` n `88`; fx avg `0.0381` n `6`; index avg `0.0476` n `25`; metal avg `-0.1214` n `20`; unknown avg `-0.4675` n `765`
- 4h: commodity avg `0.2273` n `12`; crypto_alt avg `-0.1394` n `229`; crypto_major avg `0.0526` n `8`; equity avg `0.8431` n `88`; fx avg `0.1082` n `6`; index avg `0.2124` n `25`; metal avg `-0.0725` n `20`; unknown avg `-0.7364` n `761`
- 24h: commodity avg `0.398` n `12`; crypto_alt avg `1.4432` n `228`; crypto_major avg `2.5887` n `8`; equity avg `-0.6849` n `88`; fx avg `-0.0173` n `6`; index avg `-0.0554` n `25`; metal avg `1.231` n `20`; unknown avg `6.1128` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
