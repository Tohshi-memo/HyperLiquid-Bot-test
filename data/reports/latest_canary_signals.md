# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T21:41:05.630638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `13`; crypto_alt avg `-0.1159` n `236`; crypto_major avg `-0.0833` n `8`; equity avg `-0.0103` n `151`; fx avg `-0.0045` n `6`; index avg `-0.0015` n `26`; metal avg `0.0196` n `20`; unknown avg `0.0446` n `1193`
- 1h: commodity avg `0.0566` n `13`; crypto_alt avg `0.1989` n `236`; crypto_major avg `0.2439` n `8`; equity avg `-0.0296` n `151`; fx avg `-0.0025` n `6`; index avg `0.0034` n `26`; metal avg `0.0197` n `20`; unknown avg `3.3837` n `1185`
- 4h: commodity avg `-0.06` n `13`; crypto_alt avg `0.2458` n `236`; crypto_major avg `0.2708` n `8`; equity avg `-0.6968` n `151`; fx avg `0.0057` n `6`; index avg `-0.1279` n `26`; metal avg `0.03` n `20`; unknown avg `2.6128` n `1109`
- 24h: commodity avg `0.4301` n `13`; crypto_alt avg `-1.6659` n `236`; crypto_major avg `-1.4797` n `8`; equity avg `-3.7722` n `151`; fx avg `0.0269` n `6`; index avg `-0.6274` n `26`; metal avg `-0.0816` n `20`; unknown avg `0.3282` n `896`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1615`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1134`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.109`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0769`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0722`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.069`, n `666`, weak_sample_signal
