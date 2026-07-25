# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T18:37:29.979414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1441` n `12`; crypto_alt avg `-0.0505` n `230`; crypto_major avg `0.0372` n `8`; equity avg `0.0205` n `100`; fx avg `-0.0051` n `6`; index avg `0.0017` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0931` n `774`
- 1h: commodity avg `0.0899` n `12`; crypto_alt avg `-0.025` n `230`; crypto_major avg `0.0998` n `8`; equity avg `0.0474` n `100`; fx avg `-0.0206` n `6`; index avg `0.0076` n `25`; metal avg `0.0142` n `20`; unknown avg `-0.0483` n `774`
- 4h: commodity avg `0.0528` n `12`; crypto_alt avg `0.6636` n `230`; crypto_major avg `1.0841` n `8`; equity avg `0.1973` n `100`; fx avg `-0.0295` n `6`; index avg `0.0423` n `25`; metal avg `0.0173` n `20`; unknown avg `0.287` n `774`
- 24h: commodity avg `-0.2362` n `12`; crypto_alt avg `0.5904` n `230`; crypto_major avg `1.3738` n `8`; equity avg `0.1556` n `100`; fx avg `-0.0278` n `6`; index avg `0.099` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.284` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.13`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1189`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1126`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1117`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
