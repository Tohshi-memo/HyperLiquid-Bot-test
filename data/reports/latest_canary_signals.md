# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T04:07:28.330157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0373` n `12`; crypto_alt avg `-0.0801` n `228`; crypto_major avg `0.0166` n `8`; equity avg `0.0226` n `74`; fx avg `0.0007` n `6`; index avg `0.0153` n `23`; metal avg `0.0046` n `18`; unknown avg `-0.1167` n `645`
- 1h: commodity avg `-0.0275` n `12`; crypto_alt avg `0.0238` n `228`; crypto_major avg `0.0009` n `8`; equity avg `0.0409` n `74`; fx avg `0.0042` n `6`; index avg `0.0018` n `23`; metal avg `-0.0124` n `18`; unknown avg `-0.5298` n `645`
- 4h: commodity avg `-0.0507` n `12`; crypto_alt avg `0.0479` n `228`; crypto_major avg `0.116` n `8`; equity avg `0.1548` n `74`; fx avg `0.0075` n `6`; index avg `-0.0018` n `23`; metal avg `0.0084` n `18`; unknown avg `-1.6129` n `629`
- 24h: commodity avg `-0.7174` n `12`; crypto_alt avg `1.868` n `228`; crypto_major avg `1.878` n `8`; equity avg `0.7071` n `74`; fx avg `-0.0041` n `6`; index avg `0.2685` n `23`; metal avg `0.306` n `18`; unknown avg `-1.6412` n `595`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
