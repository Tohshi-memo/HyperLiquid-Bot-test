# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T07:37:30.275521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `-0.0037` n `235`; crypto_major avg `-0.0032` n `8`; equity avg `0.0061` n `150`; fx avg `-0.003` n `6`; index avg `-0.0052` n `26`; metal avg `0.0039` n `20`; unknown avg `0.7876` n `1117`
- 1h: commodity avg `0.004` n `13`; crypto_alt avg `0.0827` n `235`; crypto_major avg `-0.0766` n `8`; equity avg `0.0246` n `150`; fx avg `-0.0052` n `6`; index avg `0.0021` n `26`; metal avg `0.0136` n `20`; unknown avg `0.7533` n `1115`
- 4h: commodity avg `-0.0054` n `13`; crypto_alt avg `0.4787` n `235`; crypto_major avg `-0.1917` n `8`; equity avg `0.0142` n `150`; fx avg `0.0009` n `6`; index avg `0.0023` n `26`; metal avg `0.011` n `20`; unknown avg `0.139` n `1093`
- 24h: commodity avg `0.1474` n `13`; crypto_alt avg `0.9854` n `235`; crypto_major avg `-0.1733` n `8`; equity avg `0.0514` n `150`; fx avg `-0.0102` n `6`; index avg `-0.0017` n `26`; metal avg `0.0119` n `20`; unknown avg `0.482` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
