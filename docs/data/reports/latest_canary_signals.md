# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T04:52:31.805866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.058` n `12`; crypto_alt avg `-0.1417` n `230`; crypto_major avg `-0.0601` n `8`; equity avg `-0.0513` n `112`; fx avg `0.0092` n `6`; index avg `-0.0093` n `25`; metal avg `-0.0383` n `20`; unknown avg `-0.019` n `785`
- 1h: commodity avg `-0.1` n `12`; crypto_alt avg `-0.1458` n `230`; crypto_major avg `-0.094` n `8`; equity avg `-0.1211` n `112`; fx avg `0.0193` n `6`; index avg `-0.0225` n `25`; metal avg `0.0244` n `20`; unknown avg `0.9268` n `785`
- 4h: commodity avg `-0.0893` n `12`; crypto_alt avg `-0.1332` n `230`; crypto_major avg `-0.0426` n `8`; equity avg `-0.2556` n `112`; fx avg `0.055` n `6`; index avg `-0.0004` n `25`; metal avg `0.0169` n `20`; unknown avg `0.5574` n `785`
- 24h: commodity avg `0.262` n `12`; crypto_alt avg `0.3649` n `230`; crypto_major avg `-0.1442` n `8`; equity avg `-0.2936` n `112`; fx avg `0.1087` n `6`; index avg `-0.0063` n `25`; metal avg `-0.1308` n `20`; unknown avg `-0.3058` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
