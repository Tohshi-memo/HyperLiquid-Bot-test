# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T16:22:27.915279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0811` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4295` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0628` n `12`; crypto_alt avg `-0.339` n `233`; crypto_major avg `-0.1663` n `8`; equity avg `-0.1507` n `135`; fx avg `0.0183` n `6`; index avg `-0.0128` n `26`; metal avg `-0.038` n `20`; unknown avg `-0.1138` n `796`
- 1h: commodity avg `0.274` n `12`; crypto_alt avg `-0.6305` n `233`; crypto_major avg `-0.4911` n `8`; equity avg `-0.3164` n `135`; fx avg `0.0343` n `6`; index avg `-0.0466` n `26`; metal avg `-0.0993` n `20`; unknown avg `-0.4069` n `794`
- 4h: commodity avg `0.4685` n `12`; crypto_alt avg `-1.2344` n `233`; crypto_major avg `-1.6126` n `8`; equity avg `-0.3488` n `135`; fx avg `0.0192` n `6`; index avg `-0.1831` n `26`; metal avg `-0.2515` n `20`; unknown avg `-0.9513` n `760`
- 24h: commodity avg `0.7925` n `12`; crypto_alt avg `-4.3845` n `233`; crypto_major avg `-3.6025` n `8`; equity avg `-1.7172` n `135`; fx avg `0.1239` n `6`; index avg `-0.2591` n `26`; metal avg `-1.0386` n `20`; unknown avg `-0.8616` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
