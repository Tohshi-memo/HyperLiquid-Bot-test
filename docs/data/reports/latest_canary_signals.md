# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T08:07:30.130721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.0522` n `233`; crypto_major avg `-0.0675` n `8`; equity avg `-0.0848` n `136`; fx avg `-0.0003` n `6`; index avg `-0.0031` n `26`; metal avg `0.0135` n `20`; unknown avg `0.0832` n `794`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `-0.2697` n `233`; crypto_major avg `-0.2768` n `8`; equity avg `-0.2196` n `136`; fx avg `0.0095` n `6`; index avg `-0.0385` n `26`; metal avg `-0.0431` n `20`; unknown avg `0.0848` n `792`
- 4h: commodity avg `-0.388` n `12`; crypto_alt avg `0.1192` n `233`; crypto_major avg `0.3292` n `8`; equity avg `0.711` n `136`; fx avg `0.0193` n `6`; index avg `0.1455` n `26`; metal avg `0.3029` n `20`; unknown avg `19.0588` n `762`
- 24h: commodity avg `0.7172` n `12`; crypto_alt avg `-1.1466` n `233`; crypto_major avg `-1.5368` n `8`; equity avg `-1.4097` n `136`; fx avg `0.0422` n `6`; index avg `-0.2369` n `26`; metal avg `-0.9568` n `20`; unknown avg `1.4187` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
