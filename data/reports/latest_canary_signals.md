# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T02:52:32.259261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `0.1494` n `230`; crypto_major avg `0.1625` n `8`; equity avg `0.0523` n `113`; fx avg `0.0032` n `6`; index avg `0.0147` n `25`; metal avg `0.0381` n `20`; unknown avg `0.1084` n `786`
- 1h: commodity avg `-0.0092` n `12`; crypto_alt avg `0.0308` n `230`; crypto_major avg `0.1576` n `8`; equity avg `0.1288` n `113`; fx avg `0.0194` n `6`; index avg `0.0208` n `25`; metal avg `-0.0144` n `20`; unknown avg `-0.1969` n `786`
- 4h: commodity avg `-0.115` n `12`; crypto_alt avg `0.4202` n `230`; crypto_major avg `0.3674` n `8`; equity avg `0.5575` n `113`; fx avg `-0.029` n `6`; index avg `0.059` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.1211` n `786`
- 24h: commodity avg `-0.2661` n `12`; crypto_alt avg `-1.5621` n `230`; crypto_major avg `-0.3875` n `8`; equity avg `2.538` n `113`; fx avg `-0.0474` n `6`; index avg `0.298` n `25`; metal avg `-0.1281` n `20`; unknown avg `0.0171` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2388`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2027`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
