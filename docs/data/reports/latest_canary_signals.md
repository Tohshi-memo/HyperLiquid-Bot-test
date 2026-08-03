# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T18:22:36.567827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0417` n `12`; crypto_alt avg `0.1639` n `230`; crypto_major avg `0.0583` n `8`; equity avg `-0.1207` n `103`; fx avg `-0.0097` n `6`; index avg `-0.0299` n `25`; metal avg `0.0417` n `20`; unknown avg `-0.0108` n `784`
- 1h: commodity avg `0.0029` n `12`; crypto_alt avg `0.2929` n `230`; crypto_major avg `0.1359` n `8`; equity avg `0.4526` n `103`; fx avg `-0.0305` n `6`; index avg `0.0636` n `25`; metal avg `0.0447` n `20`; unknown avg `-0.0802` n `784`
- 4h: commodity avg `0.1626` n `12`; crypto_alt avg `0.7206` n `230`; crypto_major avg `0.9534` n `8`; equity avg `1.8661` n `103`; fx avg `0.0083` n `6`; index avg `0.2665` n `25`; metal avg `0.1258` n `20`; unknown avg `-0.1994` n `784`
- 24h: commodity avg `-0.0653` n `12`; crypto_alt avg `0.55` n `230`; crypto_major avg `0.7961` n `8`; equity avg `2.0487` n `102`; fx avg `-0.2068` n `6`; index avg `0.0816` n `25`; metal avg `-0.4598` n `20`; unknown avg `0.1132` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
