# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T06:22:23.744518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `13`; crypto_alt avg `-0.122` n `237`; crypto_major avg `-0.0562` n `8`; equity avg `0.068` n `151`; fx avg `-0.0049` n `6`; index avg `0.0033` n `26`; metal avg `-0.0398` n `20`; unknown avg `0.3479` n `1194`
- 1h: commodity avg `-0.0641` n `13`; crypto_alt avg `0.2582` n `237`; crypto_major avg `0.1468` n `8`; equity avg `0.3855` n `151`; fx avg `-0.0027` n `6`; index avg `0.0532` n `26`; metal avg `0.0198` n `20`; unknown avg `0.0103` n `1172`
- 4h: commodity avg `-0.1034` n `13`; crypto_alt avg `0.0223` n `237`; crypto_major avg `0.3529` n `8`; equity avg `0.8317` n `151`; fx avg `0.0094` n `6`; index avg `0.1287` n `26`; metal avg `0.0445` n `20`; unknown avg `5.1479` n `1164`
- 24h: commodity avg `-0.4795` n `13`; crypto_alt avg `0.5028` n `237`; crypto_major avg `1.2109` n `8`; equity avg `3.0791` n `151`; fx avg `-0.0364` n `6`; index avg `0.56` n `26`; metal avg `0.3117` n `20`; unknown avg `3.3821` n `901`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1958`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1206`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0691`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0668`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `666`, weak_sample_signal
