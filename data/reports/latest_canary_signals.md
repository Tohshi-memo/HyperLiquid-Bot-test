# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T14:22:46.250774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `13`; crypto_alt avg `-0.1587` n `235`; crypto_major avg `-0.123` n `8`; equity avg `0.2616` n `150`; fx avg `0.0128` n `6`; index avg `0.0335` n `26`; metal avg `0.0198` n `20`; unknown avg `-0.1208` n `1076`
- 1h: commodity avg `0.0253` n `13`; crypto_alt avg `-0.1267` n `235`; crypto_major avg `-0.1518` n `8`; equity avg `0.1022` n `150`; fx avg `-0.0012` n `6`; index avg `-0.0383` n `26`; metal avg `-0.0291` n `20`; unknown avg `0.2392` n `1028`
- 4h: commodity avg `0.0964` n `13`; crypto_alt avg `-1.265` n `235`; crypto_major avg `-1.0096` n `8`; equity avg `-0.4347` n `150`; fx avg `-0.0244` n `6`; index avg `-0.1521` n `26`; metal avg `-0.2052` n `20`; unknown avg `0.323` n `1022`
- 24h: commodity avg `1.1693` n `13`; crypto_alt avg `-5.5823` n `235`; crypto_major avg `-4.1129` n `8`; equity avg `-1.93` n `150`; fx avg `-0.1513` n `6`; index avg `-0.428` n `26`; metal avg `-0.5223` n `20`; unknown avg `2.3332` n `960`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
