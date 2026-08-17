# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T17:37:34.323362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1204` n `12`; crypto_alt avg `-0.2261` n `230`; crypto_major avg `-0.2722` n `8`; equity avg `-0.097` n `114`; fx avg `0.0035` n `6`; index avg `-0.0279` n `25`; metal avg `-0.0443` n `20`; unknown avg `0.1365` n `792`
- 1h: commodity avg `0.3075` n `12`; crypto_alt avg `-0.0888` n `230`; crypto_major avg `-0.2285` n `8`; equity avg `-0.3223` n `114`; fx avg `-0.0006` n `6`; index avg `-0.0757` n `25`; metal avg `-0.0926` n `20`; unknown avg `0.2679` n `792`
- 4h: commodity avg `0.3385` n `12`; crypto_alt avg `-0.1183` n `230`; crypto_major avg `0.0438` n `8`; equity avg `0.4571` n `114`; fx avg `0.0108` n `6`; index avg `0.0003` n `25`; metal avg `0.1399` n `20`; unknown avg `0.172` n `792`
- 24h: commodity avg `0.3175` n `12`; crypto_alt avg `-0.159` n `230`; crypto_major avg `0.6383` n `8`; equity avg `1.3559` n `114`; fx avg `0.0352` n `6`; index avg `0.1213` n `25`; metal avg `0.1983` n `20`; unknown avg `0.2726` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1705`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
