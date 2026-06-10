# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T21:37:31.766754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0846` n `12`; crypto_alt avg `0.1513` n `228`; crypto_major avg `-0.1261` n `8`; equity avg `0.0752` n `74`; fx avg `0.017` n `6`; index avg `-0.0035` n `23`; metal avg `0.0029` n `18`; unknown avg `-0.0601` n `550`
- 1h: commodity avg `0.3585` n `12`; crypto_alt avg `-0.7549` n `228`; crypto_major avg `-0.4496` n `8`; equity avg `-0.1856` n `74`; fx avg `0.0033` n `6`; index avg `-0.0012` n `23`; metal avg `-0.102` n `18`; unknown avg `-0.1371` n `550`
- 4h: commodity avg `0.0244` n `12`; crypto_alt avg `-1.5486` n `228`; crypto_major avg `-1.0308` n `8`; equity avg `-1.1754` n `74`; fx avg `-0.0237` n `6`; index avg `-0.6082` n `23`; metal avg `-0.9288` n `18`; unknown avg `-0.4671` n `550`
- 24h: commodity avg `1.4657` n `12`; crypto_alt avg `-2.6328` n `228`; crypto_major avg `-2.7623` n `8`; equity avg `-2.0186` n `74`; fx avg `0.0283` n `6`; index avg `-1.528` n `23`; metal avg `-2.6082` n `18`; unknown avg `-0.5081` n `537`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
