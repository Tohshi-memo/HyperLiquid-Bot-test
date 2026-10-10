# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T04:37:30.856392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `13`; crypto_alt avg `0.1233` n `235`; crypto_major avg `0.0233` n `8`; equity avg `-0.0107` n `150`; fx avg `0.0003` n `6`; index avg `0.0019` n `26`; metal avg `-0.0005` n `20`; unknown avg `1.0017` n `1116`
- 1h: commodity avg `0.003` n `13`; crypto_alt avg `0.1487` n `235`; crypto_major avg `0.1328` n `8`; equity avg `0.0297` n `150`; fx avg `0.0075` n `6`; index avg `0.0098` n `26`; metal avg `-0.0144` n `20`; unknown avg `-0.2317` n `1108`
- 4h: commodity avg `0.0034` n `13`; crypto_alt avg `0.3694` n `235`; crypto_major avg `0.1489` n `8`; equity avg `0.0535` n `150`; fx avg `0.0069` n `6`; index avg `0.015` n `26`; metal avg `-0.0057` n `20`; unknown avg `-0.1806` n `1108`
- 24h: commodity avg `0.0617` n `13`; crypto_alt avg `1.9134` n `235`; crypto_major avg `0.1506` n `8`; equity avg `0.3617` n `150`; fx avg `-0.0009` n `6`; index avg `0.0539` n `26`; metal avg `0.124` n `20`; unknown avg `12.4661` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
