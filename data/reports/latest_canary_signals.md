# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T04:52:32.247413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0283` n `12`; crypto_alt avg `-0.01` n `228`; crypto_major avg `-0.0428` n `8`; equity avg `0.0051` n `74`; fx avg `0.0006` n `6`; index avg `0.008` n `23`; metal avg `0.0265` n `18`; unknown avg `-0.1049` n `635`
- 1h: commodity avg `0.0485` n `12`; crypto_alt avg `-0.0012` n `228`; crypto_major avg `-0.0021` n `8`; equity avg `-0.0826` n `74`; fx avg `0.0285` n `6`; index avg `-0.0605` n `23`; metal avg `0.0071` n `18`; unknown avg `0.6301` n `635`
- 4h: commodity avg `-0.0205` n `12`; crypto_alt avg `0.4542` n `228`; crypto_major avg `-0.1838` n `8`; equity avg `-0.3433` n `74`; fx avg `0.0273` n `6`; index avg `0.03` n `23`; metal avg `-0.0688` n `18`; unknown avg `-0.5153` n `635`
- 24h: commodity avg `-0.5139` n `12`; crypto_alt avg `-0.0846` n `228`; crypto_major avg `-0.5495` n `8`; equity avg `-0.9785` n `74`; fx avg `-0.0028` n `6`; index avg `0.4969` n `23`; metal avg `0.4056` n `18`; unknown avg `40.6828` n `507`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
