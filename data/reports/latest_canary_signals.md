# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T16:52:29.578376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0645` n `12`; crypto_alt avg `0.139` n `234`; crypto_major avg `0.1228` n `8`; equity avg `0.1391` n `138`; fx avg `0.0035` n `6`; index avg `0.0247` n `26`; metal avg `-0.0077` n `20`; unknown avg `1.0077` n `919`
- 1h: commodity avg `0.1444` n `12`; crypto_alt avg `0.2709` n `234`; crypto_major avg `-0.2362` n `8`; equity avg `0.1964` n `138`; fx avg `0.0176` n `6`; index avg `0.0283` n `26`; metal avg `-0.0334` n `20`; unknown avg `0.8608` n `911`
- 4h: commodity avg `0.3965` n `12`; crypto_alt avg `0.9308` n `234`; crypto_major avg `0.2906` n `8`; equity avg `0.3582` n `138`; fx avg `-0.0026` n `6`; index avg `0.0276` n `26`; metal avg `-0.0002` n `20`; unknown avg `1.7107` n `891`
- 24h: commodity avg `-0.0365` n `12`; crypto_alt avg `5.0163` n `234`; crypto_major avg `2.4847` n `8`; equity avg `1.9645` n `138`; fx avg `0.0476` n `6`; index avg `0.2741` n `26`; metal avg `0.2085` n `20`; unknown avg `1.0479` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
