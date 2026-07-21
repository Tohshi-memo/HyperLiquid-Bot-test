# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T19:07:38.880322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `12`; crypto_alt avg `0.0389` n `230`; crypto_major avg `0.0134` n `8`; equity avg `-0.0166` n `98`; fx avg `-0.002` n `6`; index avg `-0.0041` n `25`; metal avg `0.006` n `20`; unknown avg `-0.0107` n `771`
- 1h: commodity avg `0.1148` n `12`; crypto_alt avg `0.0981` n `230`; crypto_major avg `-0.0933` n `8`; equity avg `-0.3928` n `98`; fx avg `0.0034` n `6`; index avg `-0.0257` n `25`; metal avg `0.0727` n `20`; unknown avg `-0.051` n `771`
- 4h: commodity avg `0.0177` n `12`; crypto_alt avg `0.0383` n `230`; crypto_major avg `-0.3639` n `8`; equity avg `0.1433` n `98`; fx avg `0.0236` n `6`; index avg `0.0823` n `25`; metal avg `0.1043` n `20`; unknown avg `0.0054` n `771`
- 24h: commodity avg `0.331` n `12`; crypto_alt avg `0.9182` n `230`; crypto_major avg `0.7386` n `8`; equity avg `3.3572` n `98`; fx avg `0.0379` n `6`; index avg `0.5982` n `25`; metal avg `0.7722` n `20`; unknown avg `0.3137` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0899`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0542`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0537`, n `666`, weak_sample_signal
