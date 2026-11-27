# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T19:07:25.390571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0145` n `13`; crypto_alt avg `0.111` n `239`; crypto_major avg `0.1241` n `8`; equity avg `0.0433` n `168`; fx avg `0.0138` n `6`; index avg `0.0087` n `27`; metal avg `-0.0` n `20`; unknown avg `159.8113` n `1251`
- 1h: commodity avg `-0.0845` n `13`; crypto_alt avg `-0.1203` n `239`; crypto_major avg `-0.0115` n `8`; equity avg `-0.3145` n `168`; fx avg `0.0074` n `6`; index avg `-0.0134` n `27`; metal avg `-0.077` n `20`; unknown avg `161.6095` n `1238`
- 4h: commodity avg `-0.238` n `13`; crypto_alt avg `1.1444` n `239`; crypto_major avg `1.3214` n `8`; equity avg `2.0831` n `168`; fx avg `-0.0452` n `6`; index avg `0.2073` n `27`; metal avg `0.0206` n `20`; unknown avg `165.4129` n `1224`
- 24h: commodity avg `-0.6231` n `13`; crypto_alt avg `-0.0223` n `239`; crypto_major avg `0.3126` n `8`; equity avg `3.2854` n `168`; fx avg `-0.1453` n `6`; index avg `0.3232` n `27`; metal avg `0.8053` n `20`; unknown avg `193.4654` n `1037`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1292`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1021`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0939`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0837`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0807`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0772`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0606`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0588`, n `669`, weak_sample_signal
