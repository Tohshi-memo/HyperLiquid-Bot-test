# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T17:22:33.306473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.0801` n `234`; crypto_major avg `-0.0437` n `8`; equity avg `-0.1085` n `138`; fx avg `0.0037` n `6`; index avg `-0.017` n `26`; metal avg `-0.0663` n `20`; unknown avg `0.4411` n `919`
- 1h: commodity avg `0.1676` n `12`; crypto_alt avg `0.381` n `234`; crypto_major avg `0.1927` n `8`; equity avg `0.0456` n `138`; fx avg `0.0253` n `6`; index avg `0.0078` n `26`; metal avg `-0.0419` n `20`; unknown avg `0.35` n `911`
- 4h: commodity avg `0.3953` n `12`; crypto_alt avg `1.0556` n `234`; crypto_major avg `0.3952` n `8`; equity avg `0.2095` n `138`; fx avg `0.0054` n `6`; index avg `0.0155` n `26`; metal avg `-0.0659` n `20`; unknown avg `1.6421` n `891`
- 24h: commodity avg `-0.0104` n `12`; crypto_alt avg `5.5303` n `234`; crypto_major avg `3.1438` n `8`; equity avg `2.0149` n `138`; fx avg `0.0587` n `6`; index avg `0.2787` n `26`; metal avg `0.2382` n `20`; unknown avg `0.707` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
