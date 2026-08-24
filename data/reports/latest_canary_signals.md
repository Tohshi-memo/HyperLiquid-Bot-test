# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T22:52:24.896930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.0459` n `231`; crypto_major avg `-0.0607` n `8`; equity avg `-0.0323` n `122`; fx avg `-0.0023` n `6`; index avg `0.0006` n `25`; metal avg `0.0204` n `20`; unknown avg `0.1003` n `794`
- 1h: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.238` n `231`; crypto_major avg `-0.0928` n `8`; equity avg `-0.0676` n `122`; fx avg `-0.0067` n `6`; index avg `0.0019` n `25`; metal avg `0.0726` n `20`; unknown avg `-0.1357` n `794`
- 4h: commodity avg `-0.1189` n `12`; crypto_alt avg `0.1677` n `231`; crypto_major avg `0.4718` n `8`; equity avg `-0.4296` n `122`; fx avg `-0.0089` n `6`; index avg `-0.051` n `25`; metal avg `0.1707` n `20`; unknown avg `-0.4622` n `794`
- 24h: commodity avg `-0.151` n `12`; crypto_alt avg `-1.6949` n `231`; crypto_major avg `-0.9823` n `8`; equity avg `-2.8142` n `122`; fx avg `-0.0705` n `6`; index avg `-0.3527` n `25`; metal avg `0.2511` n `20`; unknown avg `1.4055` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
