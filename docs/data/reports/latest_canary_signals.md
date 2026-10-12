# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T19:24:53.383035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `13`; crypto_alt avg `0.0049` n `235`; crypto_major avg `0.0665` n `8`; equity avg `0.0472` n `151`; fx avg `0.0057` n `6`; index avg `0.0062` n `26`; metal avg `-0.0038` n `20`; unknown avg `33.0469` n `1134`
- 1h: commodity avg `-0.1308` n `13`; crypto_alt avg `-0.0099` n `235`; crypto_major avg `0.0411` n `8`; equity avg `-0.038` n `151`; fx avg `0.0018` n `6`; index avg `-0.0015` n `26`; metal avg `-0.038` n `20`; unknown avg `3.7946` n `1132`
- 4h: commodity avg `-0.0774` n `13`; crypto_alt avg `-0.774` n `235`; crypto_major avg `-0.6339` n `8`; equity avg `-0.2237` n `151`; fx avg `-0.0274` n `6`; index avg `-0.0283` n `26`; metal avg `-0.0209` n `20`; unknown avg `0.232` n `1126`
- 24h: commodity avg `0.4227` n `13`; crypto_alt avg `-3.0516` n `235`; crypto_major avg `-2.0136` n `8`; equity avg `-3.4826` n `151`; fx avg `-0.1596` n `6`; index avg `-0.348` n `26`; metal avg `-0.192` n `20`; unknown avg `-0.016` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2119`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1801`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1208`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0991`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.085`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0818`, n `666`, weak_sample_signal
