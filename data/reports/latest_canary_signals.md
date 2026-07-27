# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T00:07:28.570839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `-0.1391` n `230`; crypto_major avg `-0.2014` n `8`; equity avg `-0.4442` n `100`; fx avg `0.0289` n `6`; index avg `-0.1545` n `25`; metal avg `0.0232` n `20`; unknown avg `0.0585` n `775`
- 1h: commodity avg `-0.0429` n `12`; crypto_alt avg `-0.1616` n `230`; crypto_major avg `-0.2502` n `8`; equity avg `-0.3178` n `100`; fx avg `0.0135` n `6`; index avg `-0.0978` n `25`; metal avg `0.0896` n `20`; unknown avg `0.0426` n `775`
- 4h: commodity avg `-0.3667` n `12`; crypto_alt avg `0.8076` n `230`; crypto_major avg `0.8857` n `8`; equity avg `0.3375` n `100`; fx avg `0.012` n `6`; index avg `0.0559` n `25`; metal avg `0.2546` n `20`; unknown avg `0.1177` n `775`
- 24h: commodity avg `-0.515` n `12`; crypto_alt avg `1.6652` n `230`; crypto_major avg `1.7501` n `8`; equity avg `0.7926` n `100`; fx avg `0.0564` n `6`; index avg `0.1237` n `25`; metal avg `0.4453` n `20`; unknown avg `0.0824` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
