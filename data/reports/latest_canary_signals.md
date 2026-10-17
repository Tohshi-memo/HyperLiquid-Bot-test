# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T09:52:25.296613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `13`; crypto_alt avg `0.1118` n `236`; crypto_major avg `0.0775` n `8`; equity avg `0.0273` n `151`; fx avg `0.0014` n `6`; index avg `0.0012` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.493` n `1193`
- 1h: commodity avg `0.0004` n `13`; crypto_alt avg `-0.0669` n `236`; crypto_major avg `0.0003` n `8`; equity avg `0.0404` n `151`; fx avg `0.0057` n `6`; index avg `0.0217` n `26`; metal avg `-0.0099` n `20`; unknown avg `0.4182` n `1191`
- 4h: commodity avg `-0.1702` n `13`; crypto_alt avg `-0.3183` n `236`; crypto_major avg `0.0917` n `8`; equity avg `0.0721` n `151`; fx avg `-0.0078` n `6`; index avg `0.0232` n `26`; metal avg `0.0077` n `20`; unknown avg `0.4955` n `1157`
- 24h: commodity avg `0.4445` n `13`; crypto_alt avg `-2.0781` n `236`; crypto_major avg `-1.2653` n `8`; equity avg `-3.7035` n `151`; fx avg `0.0218` n `6`; index avg `-0.5353` n `26`; metal avg `-0.2088` n `20`; unknown avg `8.7883` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1815`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1517`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1248`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1196`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0778`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
