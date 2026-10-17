# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T13:37:26.562950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `0.0992` n `236`; crypto_major avg `0.0094` n `8`; equity avg `0.0313` n `151`; fx avg `-0.0036` n `6`; index avg `0.0161` n `26`; metal avg `0.0056` n `20`; unknown avg `3.0818` n `1193`
- 1h: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.6417` n `236`; crypto_major avg `-0.2321` n `8`; equity avg `-0.0458` n `151`; fx avg `-0.0056` n `6`; index avg `0.0003` n `26`; metal avg `-0.0081` n `20`; unknown avg `0.0084` n `1191`
- 4h: commodity avg `0.001` n `13`; crypto_alt avg `-1.2144` n `236`; crypto_major avg `-0.6588` n `8`; equity avg `-0.1582` n `151`; fx avg `0.0132` n `6`; index avg `-0.0337` n `26`; metal avg `-0.0105` n `20`; unknown avg `3.1407` n `1183`
- 24h: commodity avg `0.5272` n `13`; crypto_alt avg `-3.0517` n `236`; crypto_major avg `-1.4976` n `8`; equity avg `-2.4934` n `151`; fx avg `0.0036` n `6`; index avg `-0.4432` n `26`; metal avg `-0.2111` n `20`; unknown avg `8.8023` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1754`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1481`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1176`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0671`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0631`, n `666`, weak_sample_signal
