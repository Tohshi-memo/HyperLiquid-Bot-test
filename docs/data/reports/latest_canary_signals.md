# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T16:22:24.151977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0295` n `13`; crypto_alt avg `-0.0081` n `235`; crypto_major avg `-0.0549` n `8`; equity avg `-0.1592` n `151`; fx avg `-0.002` n `6`; index avg `-0.0213` n `26`; metal avg `0.0057` n `20`; unknown avg `-0.0526` n `1134`
- 1h: commodity avg `-0.0573` n `13`; crypto_alt avg `0.0101` n `235`; crypto_major avg `0.1133` n `8`; equity avg `0.1707` n `151`; fx avg `-0.0294` n `6`; index avg `0.0354` n `26`; metal avg `0.0244` n `20`; unknown avg `0.4786` n `1126`
- 4h: commodity avg `0.3393` n `13`; crypto_alt avg `-1.5837` n `235`; crypto_major avg `-0.8522` n `8`; equity avg `-1.5994` n `151`; fx avg `-0.0331` n `6`; index avg `-0.1061` n `26`; metal avg `-0.0768` n `20`; unknown avg `-0.0697` n `1074`
- 24h: commodity avg `0.4826` n `13`; crypto_alt avg `-2.4136` n `235`; crypto_major avg `-1.4626` n `8`; equity avg `-3.0613` n `151`; fx avg `-0.1571` n `6`; index avg `-0.2712` n `26`; metal avg `-0.1194` n `20`; unknown avg `-0.4704` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2112`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1942`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1174`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1085`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.108`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0906`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0898`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0888`, n `666`, weak_sample_signal
