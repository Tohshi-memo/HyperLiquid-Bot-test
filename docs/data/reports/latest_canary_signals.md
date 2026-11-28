# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T08:53:05.882575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `0.052` n `239`; crypto_major avg `-0.0506` n `8`; equity avg `0.0018` n `168`; fx avg `0.002` n `6`; index avg `0.0011` n `27`; metal avg `-0.005` n `20`; unknown avg `-0.4017` n `1259`
- 1h: commodity avg `-0.0095` n `13`; crypto_alt avg `-0.1126` n `239`; crypto_major avg `-0.388` n `8`; equity avg `-0.134` n `168`; fx avg `0.0027` n `6`; index avg `-0.0112` n `27`; metal avg `-0.0024` n `20`; unknown avg `-0.2237` n `1235`
- 4h: commodity avg `-0.0135` n `13`; crypto_alt avg `-1.0445` n `239`; crypto_major avg `-0.8329` n `8`; equity avg `-0.2541` n `168`; fx avg `-0.0081` n `6`; index avg `-0.0399` n `27`; metal avg `-0.0149` n `20`; unknown avg `-0.063` n `1203`
- 24h: commodity avg `-0.7182` n `13`; crypto_alt avg `-3.1432` n `239`; crypto_major avg `-2.9967` n `8`; equity avg `-0.5573` n `168`; fx avg `-0.0774` n `6`; index avg `-0.0215` n `27`; metal avg `-0.4065` n `20`; unknown avg `193.9121` n `1075`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
