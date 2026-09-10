# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T22:52:29.704326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0263` n `12`; crypto_alt avg `-0.141` n `233`; crypto_major avg `-0.1221` n `8`; equity avg `-0.0408` n `136`; fx avg `-0.0054` n `6`; index avg `-0.0072` n `26`; metal avg `0.0168` n `20`; unknown avg `-0.1905` n `788`
- 1h: commodity avg `-0.2651` n `12`; crypto_alt avg `-0.6096` n `233`; crypto_major avg `-0.4691` n `8`; equity avg `-0.1061` n `136`; fx avg `0.0028` n `6`; index avg `-0.0157` n `26`; metal avg `-0.0418` n `20`; unknown avg `0.2705` n `760`
- 4h: commodity avg `0.339` n `12`; crypto_alt avg `-0.6989` n `233`; crypto_major avg `-0.4083` n `8`; equity avg `-0.563` n `136`; fx avg `0.0262` n `6`; index avg `-0.0448` n `26`; metal avg `-0.1369` n `20`; unknown avg `-0.2871` n `716`
- 24h: commodity avg `1.1341` n `12`; crypto_alt avg `-1.4887` n `233`; crypto_major avg `-1.6324` n `8`; equity avg `-2.0739` n `136`; fx avg `0.1357` n `6`; index avg `-0.3455` n `26`; metal avg `-1.2959` n `20`; unknown avg `-0.9987` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
