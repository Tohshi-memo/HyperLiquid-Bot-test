# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T05:37:30.981329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `5`; crypto_alt avg `-0.0136` n `235`; crypto_major avg `-0.0241` n `8`; equity avg `0.0025` n `41`; fx avg `0.0` n `1`; index avg `0.0` n `17`; metal avg `0.0` n `12`; unknown avg `-0.1987` n `1087`
- 1h: commodity avg `-0.0479` n `13`; crypto_alt avg `0.2152` n `235`; crypto_major avg `-0.0063` n `8`; equity avg `0.0103` n `150`; fx avg `-0.0003` n `6`; index avg `0.0002` n `26`; metal avg `-0.0036` n `20`; unknown avg `0.003` n `1115`
- 4h: commodity avg `0.087` n `13`; crypto_alt avg `-0.6422` n `235`; crypto_major avg `-0.3528` n `8`; equity avg `-0.0717` n `150`; fx avg `0.0038` n `6`; index avg `-0.0117` n `26`; metal avg `-0.0073` n `20`; unknown avg `-0.0407` n `1109`
- 24h: commodity avg `0.1246` n `13`; crypto_alt avg `0.2682` n `235`; crypto_major avg `-0.2337` n `8`; equity avg `-0.0333` n `150`; fx avg `-0.0114` n `6`; index avg `-0.0418` n `26`; metal avg `0.001` n `20`; unknown avg `0.2516` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
