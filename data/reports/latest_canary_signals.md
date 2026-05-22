# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T22:52:17.639534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `0.0263` n `228`; crypto_major avg `0.0161` n `8`; equity avg `-0.0352` n `67`; fx avg `0.0023` n `6`; index avg `0.0396` n `23`; metal avg `-0.0241` n `18`; unknown avg `1.061` n `386`
- 1h: commodity avg `0.1138` n `12`; crypto_alt avg `-0.6162` n `228`; crypto_major avg `-0.4745` n `8`; equity avg `-0.1669` n `67`; fx avg `0.0065` n `6`; index avg `0.0361` n `23`; metal avg `-0.0233` n `18`; unknown avg `0.5529` n `386`
- 4h: commodity avg `0.5776` n `12`; crypto_alt avg `-1.0981` n `228`; crypto_major avg `-0.8405` n `8`; equity avg `-0.7884` n `67`; fx avg `0.0275` n `6`; index avg `-0.2913` n `23`; metal avg `-0.2422` n `18`; unknown avg `1.5773` n `386`
- 24h: commodity avg `-0.636` n `12`; crypto_alt avg `-2.9394` n `228`; crypto_major avg `-2.1704` n `8`; equity avg `-1.471` n `67`; fx avg `0.1476` n `6`; index avg `0.385` n `23`; metal avg `-1.109` n `18`; unknown avg `-0.5709` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
