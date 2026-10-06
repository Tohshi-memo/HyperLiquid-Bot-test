# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T16:52:41.965705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0342` n `13`; crypto_alt avg `0.1577` n `235`; crypto_major avg `0.1836` n `8`; equity avg `0.0103` n `150`; fx avg `-0.0011` n `6`; index avg `0.002` n `26`; metal avg `-0.0148` n `20`; unknown avg `0.1079` n `1076`
- 1h: commodity avg `0.1338` n `13`; crypto_alt avg `-0.4288` n `235`; crypto_major avg `-0.3042` n `8`; equity avg `-0.2142` n `150`; fx avg `-0.0107` n `6`; index avg `-0.0508` n `26`; metal avg `-0.0569` n `20`; unknown avg `0.6096` n `1068`
- 4h: commodity avg `0.4883` n `13`; crypto_alt avg `-0.4194` n `235`; crypto_major avg `-0.5052` n `8`; equity avg `0.0832` n `150`; fx avg `-0.0112` n `6`; index avg `-0.0477` n `26`; metal avg `-0.0069` n `20`; unknown avg `5.6969` n `1018`
- 24h: commodity avg `-0.1768` n `13`; crypto_alt avg `0.2669` n `235`; crypto_major avg `0.093` n `8`; equity avg `0.7226` n `149`; fx avg `0.1111` n `6`; index avg `0.0762` n `26`; metal avg `0.0199` n `20`; unknown avg `381.2081` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
