# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T18:22:34.466206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0599` n `12`; crypto_alt avg `0.2722` n `228`; crypto_major avg `0.2721` n `8`; equity avg `0.0717` n `86`; fx avg `-0.0039` n `6`; index avg `-0.001` n `23`; metal avg `-0.0057` n `20`; unknown avg `-0.0039` n `764`
- 1h: commodity avg `-0.0329` n `12`; crypto_alt avg `-0.1076` n `228`; crypto_major avg `-0.1146` n `8`; equity avg `-0.4411` n `86`; fx avg `-0.0084` n `6`; index avg `-0.0891` n `23`; metal avg `-0.1661` n `20`; unknown avg `-0.273` n `764`
- 4h: commodity avg `0.0012` n `12`; crypto_alt avg `-0.6958` n `228`; crypto_major avg `-0.5332` n `8`; equity avg `-0.8807` n `86`; fx avg `-0.057` n `6`; index avg `-0.2356` n `23`; metal avg `-0.1121` n `20`; unknown avg `-0.7975` n `764`
- 24h: commodity avg `-0.4056` n `12`; crypto_alt avg `-3.9422` n `228`; crypto_major avg `-4.7377` n `8`; equity avg `-3.6238` n `86`; fx avg `-0.1845` n `6`; index avg `-0.9514` n `23`; metal avg `-1.1256` n `20`; unknown avg `-0.4746` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
