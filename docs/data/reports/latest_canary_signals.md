# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T17:52:28.078358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `0.0071` n `230`; crypto_major avg `-0.0362` n `8`; equity avg `-0.0201` n `96`; fx avg `0.0` n `6`; index avg `-0.0001` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0062` n `771`
- 1h: commodity avg `-0.0356` n `12`; crypto_alt avg `-0.0932` n `230`; crypto_major avg `0.0877` n `8`; equity avg `0.0959` n `96`; fx avg `0.0051` n `6`; index avg `0.0292` n `25`; metal avg `0.0361` n `20`; unknown avg `0.0128` n `770`
- 4h: commodity avg `-0.0196` n `12`; crypto_alt avg `-0.1922` n `230`; crypto_major avg `-0.1059` n `8`; equity avg `-0.0085` n `96`; fx avg `0.0073` n `6`; index avg `-0.053` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.0536` n `770`
- 24h: commodity avg `0.1001` n `12`; crypto_alt avg `-0.1898` n `230`; crypto_major avg `0.4332` n `8`; equity avg `0.3218` n `96`; fx avg `0.0561` n `6`; index avg `-0.073` n `25`; metal avg `-0.0186` n `20`; unknown avg `0.0256` n `752`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1451`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1409`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1025`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
