# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T06:07:22.496047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `12`; crypto_alt avg `-0.1396` n `228`; crypto_major avg `-0.1343` n `8`; equity avg `-0.0102` n `69`; fx avg `-0.0006` n `6`; index avg `0.0027` n `23`; metal avg `-0.0202` n `18`; unknown avg `0.7054` n `401`
- 1h: commodity avg `-0.0197` n `12`; crypto_alt avg `-0.3623` n `228`; crypto_major avg `-0.1868` n `8`; equity avg `0.0611` n `69`; fx avg `0.0` n `6`; index avg `0.0036` n `23`; metal avg `0.0119` n `18`; unknown avg `-0.2135` n `401`
- 4h: commodity avg `0.0218` n `12`; crypto_alt avg `-0.1789` n `228`; crypto_major avg `0.1375` n `8`; equity avg `0.1502` n `69`; fx avg `0.0136` n `6`; index avg `-0.0458` n `23`; metal avg `-0.033` n `18`; unknown avg `-0.053` n `401`
- 24h: commodity avg `0.1237` n `12`; crypto_alt avg `0.4028` n `228`; crypto_major avg `2.2463` n `8`; equity avg `0.9479` n `69`; fx avg `0.0412` n `6`; index avg `0.0015` n `23`; metal avg `-0.0389` n `18`; unknown avg `0.462` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
