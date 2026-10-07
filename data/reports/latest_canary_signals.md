# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T20:52:33.967707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0402` n `13`; crypto_alt avg `0.0794` n `235`; crypto_major avg `0.0714` n `8`; equity avg `0.0362` n `150`; fx avg `-0.0003` n `6`; index avg `0.0092` n `26`; metal avg `-0.017` n `20`; unknown avg `0.0281` n `1077`
- 1h: commodity avg `0.0627` n `13`; crypto_alt avg `0.2285` n `235`; crypto_major avg `0.1525` n `8`; equity avg `0.0327` n `150`; fx avg `0.0055` n `6`; index avg `-0.0062` n `26`; metal avg `0.0296` n `20`; unknown avg `0.4961` n `1005`
- 4h: commodity avg `0.0288` n `13`; crypto_alt avg `0.2642` n `235`; crypto_major avg `-0.2503` n `8`; equity avg `0.1671` n `150`; fx avg `0.0124` n `6`; index avg `0.0279` n `26`; metal avg `-0.0896` n `20`; unknown avg `0.8685` n `1004`
- 24h: commodity avg `0.3409` n `13`; crypto_alt avg `-4.1287` n `235`; crypto_major avg `-3.4408` n `8`; equity avg `-1.4038` n `150`; fx avg `-0.1525` n `6`; index avg `-0.2206` n `26`; metal avg `-0.6995` n `20`; unknown avg `1.2937` n `972`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
