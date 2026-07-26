# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T20:07:26.267770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0296` n `12`; crypto_alt avg `0.0062` n `230`; crypto_major avg `0.0101` n `8`; equity avg `-0.0475` n `100`; fx avg `-0.0079` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0162` n `20`; unknown avg `-0.0091` n `775`
- 1h: commodity avg `0.0541` n `12`; crypto_alt avg `-0.022` n `230`; crypto_major avg `0.0035` n `8`; equity avg `-0.0972` n `100`; fx avg `0.0168` n `6`; index avg `-0.01` n `25`; metal avg `-0.0227` n `20`; unknown avg `-0.2382` n `775`
- 4h: commodity avg `0.2193` n `12`; crypto_alt avg `-0.1892` n `230`; crypto_major avg `-0.0672` n `8`; equity avg `-0.0471` n `100`; fx avg `0.0129` n `6`; index avg `-0.0282` n `25`; metal avg `0.0319` n `20`; unknown avg `-0.407` n `775`
- 24h: commodity avg `-0.1869` n `12`; crypto_alt avg `0.7628` n `230`; crypto_major avg `0.7421` n `8`; equity avg `0.5871` n `100`; fx avg `0.0436` n `6`; index avg `0.1054` n `25`; metal avg `0.1882` n `20`; unknown avg `-0.1092` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
