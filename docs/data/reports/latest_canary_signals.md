# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T16:22:29.420137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0569` n `12`; crypto_alt avg `-0.0377` n `232`; crypto_major avg `-0.1163` n `8`; equity avg `0.1101` n `128`; fx avg `-0.0015` n `6`; index avg `0.0157` n `26`; metal avg `0.0186` n `20`; unknown avg `0.0401` n `794`
- 1h: commodity avg `0.0658` n `12`; crypto_alt avg `-0.0463` n `232`; crypto_major avg `0.0848` n `8`; equity avg `-0.0752` n `128`; fx avg `-0.0167` n `6`; index avg `-0.0334` n `26`; metal avg `-0.0016` n `20`; unknown avg `0.0009` n `792`
- 4h: commodity avg `0.1139` n `12`; crypto_alt avg `-0.4299` n `232`; crypto_major avg `-0.0509` n `8`; equity avg `-0.1316` n `128`; fx avg `0.0247` n `6`; index avg `-0.1355` n `26`; metal avg `-0.2444` n `20`; unknown avg `-0.0438` n `790`
- 24h: commodity avg `0.6124` n `12`; crypto_alt avg `-1.5181` n `231`; crypto_major avg `-2.0277` n `8`; equity avg `-0.6352` n `128`; fx avg `-0.0954` n `6`; index avg `-0.232` n `26`; metal avg `-0.5452` n `20`; unknown avg `0.0547` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
