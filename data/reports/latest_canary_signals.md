# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T11:37:30.566712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `0.0172` n `230`; crypto_major avg `0.0309` n `8`; equity avg `0.0401` n `94`; fx avg `0.0074` n `6`; index avg `-0.0024` n `25`; metal avg `0.0266` n `20`; unknown avg `-0.0835` n `768`
- 1h: commodity avg `-0.027` n `12`; crypto_alt avg `-0.1062` n `230`; crypto_major avg `-0.127` n `8`; equity avg `-0.241` n `94`; fx avg `-0.0089` n `6`; index avg `-0.0562` n `25`; metal avg `-0.068` n `20`; unknown avg `-0.0234` n `768`
- 4h: commodity avg `0.0505` n `12`; crypto_alt avg `-0.371` n `230`; crypto_major avg `-0.4763` n `8`; equity avg `-0.6666` n `94`; fx avg `-0.0474` n `6`; index avg `-0.1163` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.2203` n `762`
- 24h: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.7593` n `230`; crypto_major avg `-0.8896` n `8`; equity avg `-3.0731` n `93`; fx avg `0.018` n `6`; index avg `-0.5281` n `25`; metal avg `-0.0171` n `20`; unknown avg `-0.0748` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
