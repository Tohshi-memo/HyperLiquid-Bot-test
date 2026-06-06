# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T13:07:22.691067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0638` n `12`; crypto_alt avg `0.0898` n `228`; crypto_major avg `-0.1543` n `8`; equity avg `-0.0001` n `74`; fx avg `-0.0003` n `6`; index avg `0.1015` n `23`; metal avg `-0.0039` n `18`; unknown avg `0.2194` n `425`
- 1h: commodity avg `0.0489` n `12`; crypto_alt avg `0.4672` n `228`; crypto_major avg `0.2161` n `8`; equity avg `0.3804` n `74`; fx avg `-0.0031` n `6`; index avg `0.3046` n `23`; metal avg `0.0262` n `18`; unknown avg `0.228` n `425`
- 4h: commodity avg `-0.0228` n `12`; crypto_alt avg `-0.1939` n `228`; crypto_major avg `-0.3863` n `8`; equity avg `0.6611` n `74`; fx avg `0.0058` n `6`; index avg `0.0769` n `23`; metal avg `-0.0247` n `18`; unknown avg `0.9415` n `421`
- 24h: commodity avg `-0.7716` n `12`; crypto_alt avg `-2.944` n `228`; crypto_major avg `-3.2801` n `8`; equity avg `-5.5869` n `74`; fx avg `-0.2348` n `6`; index avg `-3.2893` n `23`; metal avg `-3.3555` n `18`; unknown avg `-0.3991` n `410`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
