# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T18:37:30.496544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0298` n `12`; crypto_alt avg `0.0525` n `230`; crypto_major avg `-0.0369` n `8`; equity avg `-0.0281` n `98`; fx avg `-0.0035` n `6`; index avg `-0.0058` n `25`; metal avg `0.0528` n `20`; unknown avg `0.0326` n `771`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `0.1543` n `230`; crypto_major avg `-0.0383` n `8`; equity avg `-0.1208` n `98`; fx avg `-0.0011` n `6`; index avg `-0.0014` n `25`; metal avg `0.0808` n `20`; unknown avg `0.0176` n `771`
- 4h: commodity avg `-0.1434` n `12`; crypto_alt avg `-0.0286` n `230`; crypto_major avg `-0.4844` n `8`; equity avg `0.5628` n `98`; fx avg `0.0067` n `6`; index avg `0.1402` n `25`; metal avg `0.108` n `20`; unknown avg `0.1053` n `771`
- 24h: commodity avg `0.2808` n `12`; crypto_alt avg `0.6337` n `230`; crypto_major avg `0.4233` n `8`; equity avg `3.077` n `98`; fx avg `0.0238` n `6`; index avg `0.5289` n `25`; metal avg `0.7349` n `20`; unknown avg `0.1202` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0896`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.054`, n `666`, weak_sample_signal
