# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T23:07:27.926519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `13`; crypto_alt avg `-0.3886` n `239`; crypto_major avg `-0.3332` n `8`; equity avg `-0.238` n `168`; fx avg `-0.0048` n `6`; index avg `-0.002` n `27`; metal avg `-0.0686` n `20`; unknown avg `0.2238` n `1225`
- 1h: commodity avg `0.0532` n `13`; crypto_alt avg `-0.4532` n `239`; crypto_major avg `-0.4292` n `8`; equity avg `-0.4012` n `168`; fx avg `0.0037` n `6`; index avg `-0.0248` n `27`; metal avg `-0.0911` n `20`; unknown avg `218.3087` n `1221`
- 4h: commodity avg `0.0179` n `13`; crypto_alt avg `-0.4104` n `239`; crypto_major avg `-0.3252` n `8`; equity avg `-0.1179` n `168`; fx avg `0.0003` n `6`; index avg `0.0029` n `27`; metal avg `-0.0465` n `20`; unknown avg `0.3158` n `1143`
- 24h: commodity avg `0.1454` n `13`; crypto_alt avg `1.4166` n `239`; crypto_major avg `0.8316` n `8`; equity avg `1.0125` n `168`; fx avg `-0.0138` n `6`; index avg `0.0964` n `27`; metal avg `0.0228` n `20`; unknown avg `182.8121` n `993`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
