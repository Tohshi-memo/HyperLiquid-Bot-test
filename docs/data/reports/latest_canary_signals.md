# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T21:07:41.477019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0348` n `13`; crypto_alt avg `-0.0025` n `235`; crypto_major avg `-0.0197` n `8`; equity avg `0.0271` n `150`; fx avg `0.0022` n `6`; index avg `0.0089` n `26`; metal avg `0.0078` n `20`; unknown avg `-0.0262` n `1068`
- 1h: commodity avg `0.0092` n `13`; crypto_alt avg `-0.0112` n `235`; crypto_major avg `0.0422` n `8`; equity avg `0.1116` n `150`; fx avg `-0.0054` n `6`; index avg `0.0253` n `26`; metal avg `-0.0237` n `20`; unknown avg `1.8005` n `1020`
- 4h: commodity avg `0.325` n `13`; crypto_alt avg `-0.2366` n `235`; crypto_major avg `-0.1215` n `8`; equity avg `-0.0783` n `150`; fx avg `-0.0061` n `6`; index avg `-0.0374` n `26`; metal avg `0.0282` n `20`; unknown avg `0.8508` n `1006`
- 24h: commodity avg `0.3113` n `13`; crypto_alt avg `-1.0537` n `235`; crypto_major avg `-0.6944` n `8`; equity avg `0.4441` n `149`; fx avg `0.1005` n `6`; index avg `-0.0003` n `26`; metal avg `0.0478` n `20`; unknown avg `862.6697` n `922`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
