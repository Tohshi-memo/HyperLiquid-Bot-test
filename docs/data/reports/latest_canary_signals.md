# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T14:37:28.752700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `13`; crypto_alt avg `0.0086` n `236`; crypto_major avg `0.0202` n `8`; equity avg `0.1514` n `151`; fx avg `0.0009` n `6`; index avg `0.0276` n `26`; metal avg `-0.0132` n `20`; unknown avg `1.9216` n `1128`
- 1h: commodity avg `-0.1967` n `13`; crypto_alt avg `0.2168` n `236`; crypto_major avg `0.5426` n `8`; equity avg `0.0102` n `151`; fx avg `0.032` n `6`; index avg `0.0017` n `26`; metal avg `0.0434` n `20`; unknown avg `2.7144` n `1064`
- 4h: commodity avg `-0.3419` n `13`; crypto_alt avg `-0.2374` n `236`; crypto_major avg `-0.0173` n `8`; equity avg `-1.2975` n `151`; fx avg `0.0349` n `6`; index avg `-0.149` n `26`; metal avg `-0.0128` n `20`; unknown avg `2.0341` n `1058`
- 24h: commodity avg `-0.4917` n `13`; crypto_alt avg `3.3806` n `236`; crypto_major avg `2.0417` n `8`; equity avg `1.4323` n `151`; fx avg `0.0347` n `6`; index avg `0.1208` n `26`; metal avg `0.2832` n `20`; unknown avg `0.5032` n `930`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.104`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0993`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0842`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0795`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
