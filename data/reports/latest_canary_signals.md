# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T21:41:09.853620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.3502` n `231`; crypto_major avg `-0.3827` n `8`; equity avg `-0.0283` n `122`; fx avg `0.0048` n `6`; index avg `0.0018` n `25`; metal avg `-0.0291` n `20`; unknown avg `0.3834` n `793`
- 1h: commodity avg `-0.0355` n `12`; crypto_alt avg `0.5929` n `231`; crypto_major avg `0.6255` n `8`; equity avg `0.0422` n `122`; fx avg `-0.0301` n `6`; index avg `0.0042` n `25`; metal avg `-0.0259` n `20`; unknown avg `1.5357` n `793`
- 4h: commodity avg `-0.0732` n `12`; crypto_alt avg `0.768` n `231`; crypto_major avg `0.7364` n `8`; equity avg `0.2218` n `122`; fx avg `-0.113` n `6`; index avg `0.0496` n `25`; metal avg `0.0255` n `20`; unknown avg `3.3228` n `793`
- 24h: commodity avg `-0.1518` n `12`; crypto_alt avg `4.6228` n `231`; crypto_major avg `2.0747` n `8`; equity avg `0.8377` n `122`; fx avg `-0.1012` n `6`; index avg `0.1342` n `25`; metal avg `0.0729` n `20`; unknown avg `8.7079` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
