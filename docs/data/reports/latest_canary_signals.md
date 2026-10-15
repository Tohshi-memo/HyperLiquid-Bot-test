# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T05:07:24.091265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0472` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0367` n `13`; crypto_alt avg `-0.4835` n `236`; crypto_major avg `-0.3648` n `8`; equity avg `0.0146` n `151`; fx avg `0.0113` n `6`; index avg `0.0088` n `26`; metal avg `0.0037` n `20`; unknown avg `0.1479` n `1134`
- 1h: commodity avg `0.0074` n `13`; crypto_alt avg `0.595` n `236`; crypto_major avg `0.7003` n `8`; equity avg `0.7727` n `151`; fx avg `-0.0017` n `6`; index avg `0.1427` n `26`; metal avg `0.056` n `20`; unknown avg `1.6934` n `1134`
- 4h: commodity avg `-0.1424` n `13`; crypto_alt avg `-2.2336` n `236`; crypto_major avg `-1.0248` n `8`; equity avg `0.1202` n `151`; fx avg `0.0279` n `6`; index avg `0.0224` n `26`; metal avg `-0.0376` n `20`; unknown avg `0.5926` n `1128`
- 24h: commodity avg `-0.4338` n `13`; crypto_alt avg `-5.1364` n `236`; crypto_major avg `-3.4019` n `8`; equity avg `-5.5401` n `151`; fx avg `0.104` n `6`; index avg `-0.9366` n `26`; metal avg `-0.7526` n `20`; unknown avg `1392.8113` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1112`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0987`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0962`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0936`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0689`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0614`, n `666`, weak_sample_signal
