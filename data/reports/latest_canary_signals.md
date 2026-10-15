# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T19:37:31.447064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0156` n `13`; crypto_alt avg `-0.1219` n `236`; crypto_major avg `-0.208` n `8`; equity avg `0.0613` n `151`; fx avg `-0.0043` n `6`; index avg `-0.0081` n `26`; metal avg `0.0021` n `20`; unknown avg `18.4417` n `1136`
- 1h: commodity avg `-0.11` n `13`; crypto_alt avg `0.248` n `236`; crypto_major avg `0.1445` n `8`; equity avg `1.1164` n `151`; fx avg `-0.0148` n `6`; index avg `0.1393` n `26`; metal avg `0.0197` n `20`; unknown avg `2.1076` n `1134`
- 4h: commodity avg `-0.1559` n `13`; crypto_alt avg `0.9708` n `236`; crypto_major avg `0.3264` n `8`; equity avg `1.377` n `151`; fx avg `0.0019` n `6`; index avg `0.1647` n `26`; metal avg `0.056` n `20`; unknown avg `1.0241` n `1128`
- 24h: commodity avg `-0.0901` n `13`; crypto_alt avg `1.1814` n `236`; crypto_major avg `0.6569` n `8`; equity avg `-0.0971` n `151`; fx avg `0.1837` n `6`; index avg `-0.0846` n `26`; metal avg `0.4646` n `20`; unknown avg `0.8787` n `940`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0989`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0934`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0843`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0791`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0759`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0606`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0501`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
