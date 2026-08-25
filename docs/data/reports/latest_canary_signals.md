# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T08:07:28.194726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `0.0481` n `231`; crypto_major avg `-0.0647` n `8`; equity avg `-0.0819` n `122`; fx avg `0.0051` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0498` n `20`; unknown avg `-0.053` n `794`
- 1h: commodity avg `0.1047` n `12`; crypto_alt avg `-0.979` n `231`; crypto_major avg `-1.0221` n `8`; equity avg `-0.2952` n `122`; fx avg `0.0134` n `6`; index avg `-0.0421` n `25`; metal avg `-0.1009` n `20`; unknown avg `-0.1531` n `794`
- 4h: commodity avg `-0.1789` n `12`; crypto_alt avg `-0.8854` n `231`; crypto_major avg `-0.7684` n `8`; equity avg `0.2927` n `122`; fx avg `0.0444` n `6`; index avg `0.0646` n `25`; metal avg `-0.0658` n `20`; unknown avg `-0.2577` n `778`
- 24h: commodity avg `-0.2411` n `12`; crypto_alt avg `0.6116` n `231`; crypto_major avg `1.789` n `8`; equity avg `0.0946` n `122`; fx avg `0.0324` n `6`; index avg `0.0367` n `25`; metal avg `-0.2639` n `20`; unknown avg `0.3835` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
