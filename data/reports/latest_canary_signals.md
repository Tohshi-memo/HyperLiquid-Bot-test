# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T21:52:33.096067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0279` n `13`; crypto_alt avg `-0.1205` n `235`; crypto_major avg `-0.0896` n `8`; equity avg `0.0027` n `150`; fx avg `0.0097` n `6`; index avg `0.0009` n `26`; metal avg `0.0024` n `20`; unknown avg `1.2632` n `1077`
- 1h: commodity avg `0.009` n `13`; crypto_alt avg `-0.3805` n `235`; crypto_major avg `-0.4192` n `8`; equity avg `0.0151` n `150`; fx avg `0.0132` n `6`; index avg `-0.0003` n `26`; metal avg `0.0372` n `20`; unknown avg `-0.2338` n `1067`
- 4h: commodity avg `0.45` n `13`; crypto_alt avg `0.5578` n `235`; crypto_major avg `-0.0178` n `8`; equity avg `0.1058` n `150`; fx avg `0.042` n `6`; index avg `0.0038` n `26`; metal avg `-0.0216` n `20`; unknown avg `0.1888` n `999`
- 24h: commodity avg `0.3815` n `13`; crypto_alt avg `-4.331` n `235`; crypto_major avg `-3.6812` n `8`; equity avg `-1.4199` n `150`; fx avg `-0.1437` n `6`; index avg `-0.2323` n `26`; metal avg `-0.6824` n `20`; unknown avg `1.1752` n `974`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
