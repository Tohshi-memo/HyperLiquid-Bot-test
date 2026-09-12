# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T20:52:35.597714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.0634` n `233`; crypto_major avg `-0.0441` n `8`; equity avg `0.0306` n `136`; fx avg `-0.0025` n `6`; index avg `0.0073` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.2978` n `838`
- 1h: commodity avg `-0.0082` n `12`; crypto_alt avg `0.151` n `233`; crypto_major avg `0.1227` n `8`; equity avg `-0.0715` n `136`; fx avg `-0.0027` n `6`; index avg `-0.0097` n `26`; metal avg `-0.0175` n `20`; unknown avg `19.7408` n `830`
- 4h: commodity avg `0.037` n `12`; crypto_alt avg `-0.3142` n `233`; crypto_major avg `-0.3992` n `8`; equity avg `-0.3125` n `136`; fx avg `-0.0035` n `6`; index avg `-0.0449` n `26`; metal avg `-0.0167` n `20`; unknown avg `7.2851` n `782`
- 24h: commodity avg `-0.1126` n `12`; crypto_alt avg `1.0412` n `233`; crypto_major avg `-0.1559` n `8`; equity avg `-0.2482` n `136`; fx avg `-0.0171` n `6`; index avg `0.0096` n `26`; metal avg `0.0018` n `20`; unknown avg `2.0132` n `736`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0486`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
