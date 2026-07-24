# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T08:52:30.928766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0537` n `12`; crypto_alt avg `-0.0979` n `230`; crypto_major avg `-0.0955` n `8`; equity avg `-0.1075` n `100`; fx avg `-0.002` n `6`; index avg `-0.0124` n `25`; metal avg `0.0084` n `20`; unknown avg `-0.0109` n `772`
- 1h: commodity avg `-0.1463` n `12`; crypto_alt avg `-0.1211` n `230`; crypto_major avg `-0.0713` n `8`; equity avg `-0.0775` n `100`; fx avg `-0.0405` n `6`; index avg `0.0127` n `25`; metal avg `0.0426` n `20`; unknown avg `0.0292` n `772`
- 4h: commodity avg `-0.4346` n `12`; crypto_alt avg `0.2665` n `230`; crypto_major avg `0.4857` n `8`; equity avg `0.4833` n `100`; fx avg `-0.0213` n `6`; index avg `0.124` n `25`; metal avg `0.2603` n `20`; unknown avg `0.119` n `756`
- 24h: commodity avg `-0.1308` n `12`; crypto_alt avg `-0.9753` n `230`; crypto_major avg `-1.2543` n `8`; equity avg `-1.8571` n `99`; fx avg `-0.1506` n `6`; index avg `-0.439` n `25`; metal avg `-0.3863` n `20`; unknown avg `0.0929` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0988`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0889`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0823`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0812`, n `666`, weak_sample_signal
