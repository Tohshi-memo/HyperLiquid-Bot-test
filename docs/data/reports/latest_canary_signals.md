# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T04:57:10.689135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0515` n `12`; crypto_alt avg `-0.0831` n `230`; crypto_major avg `-0.1272` n `8`; equity avg `-0.0182` n `98`; fx avg `0.0003` n `6`; index avg `-0.0329` n `25`; metal avg `-0.0692` n `20`; unknown avg `0.0337` n `773`
- 1h: commodity avg `-0.0284` n `12`; crypto_alt avg `0.1747` n `230`; crypto_major avg `-0.0149` n `8`; equity avg `0.0109` n `98`; fx avg `0.0107` n `6`; index avg `0.0175` n `25`; metal avg `-0.0371` n `20`; unknown avg `-0.1703` n `773`
- 4h: commodity avg `0.0925` n `12`; crypto_alt avg `-0.5445` n `230`; crypto_major avg `-0.6394` n `8`; equity avg `-0.3526` n `98`; fx avg `-0.0272` n `6`; index avg `-0.0633` n `25`; metal avg `0.0464` n `20`; unknown avg `0.5145` n `773`
- 24h: commodity avg `0.741` n `12`; crypto_alt avg `-0.6792` n `230`; crypto_major avg `-0.8965` n `8`; equity avg `-0.3379` n `98`; fx avg `-0.148` n `6`; index avg `-0.0147` n `25`; metal avg `-0.0659` n `20`; unknown avg `1.5846` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0801`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
