# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T19:22:26.794005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.039` n `13`; crypto_alt avg `0.0298` n `235`; crypto_major avg `0.0046` n `8`; equity avg `0.107` n `151`; fx avg `-0.0032` n `6`; index avg `0.0161` n `26`; metal avg `-0.0149` n `20`; unknown avg `0.4696` n `1135`
- 1h: commodity avg `0.0575` n `13`; crypto_alt avg `0.5364` n `235`; crypto_major avg `0.3679` n `8`; equity avg `0.0293` n `151`; fx avg `0.0036` n `6`; index avg `0.0101` n `26`; metal avg `-0.0133` n `20`; unknown avg `-0.0032` n `1133`
- 4h: commodity avg `0.2757` n `13`; crypto_alt avg `0.1561` n `235`; crypto_major avg `-0.1468` n `8`; equity avg `0.4682` n `151`; fx avg `0.0068` n `6`; index avg `0.083` n `26`; metal avg `-0.0722` n `20`; unknown avg `1.1628` n `1127`
- 24h: commodity avg `0.6476` n `13`; crypto_alt avg `-1.1098` n `235`; crypto_major avg `-0.1202` n `8`; equity avg `-0.7859` n `151`; fx avg `0.1698` n `6`; index avg `-0.1482` n `26`; metal avg `-0.2074` n `20`; unknown avg `0.7967` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1614`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1448`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1194`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0921`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0831`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
