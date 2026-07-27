# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T05:37:31.083687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0434` n `12`; crypto_alt avg `-0.0915` n `230`; crypto_major avg `-0.1068` n `8`; equity avg `-0.0462` n `100`; fx avg `-0.0051` n `6`; index avg `0.01` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.045` n `775`
- 1h: commodity avg `0.0422` n `12`; crypto_alt avg `-0.0151` n `230`; crypto_major avg `-0.0079` n `8`; equity avg `0.2193` n `100`; fx avg `0.0036` n `6`; index avg `0.0931` n `25`; metal avg `-0.007` n `20`; unknown avg `-0.1016` n `775`
- 4h: commodity avg `-0.0623` n `12`; crypto_alt avg `0.2917` n `230`; crypto_major avg `0.5449` n `8`; equity avg `0.9204` n `100`; fx avg `0.0123` n `6`; index avg `0.1593` n `25`; metal avg `-0.0722` n `20`; unknown avg `-0.4256` n `775`
- 24h: commodity avg `-0.5014` n `12`; crypto_alt avg `1.0916` n `230`; crypto_major avg `1.2748` n `8`; equity avg `1.0639` n `100`; fx avg `0.0791` n `6`; index avg `0.1758` n `25`; metal avg `0.3336` n `20`; unknown avg `-0.0217` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
