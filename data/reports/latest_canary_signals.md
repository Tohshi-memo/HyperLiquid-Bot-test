# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T01:07:31.926617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0394` n `13`; crypto_alt avg `-0.1171` n `235`; crypto_major avg `-0.2076` n `8`; equity avg `-0.11` n `150`; fx avg `-0.0224` n `6`; index avg `-0.0246` n `26`; metal avg `0.1082` n `20`; unknown avg `0.0613` n `1076`
- 1h: commodity avg `-0.0578` n `13`; crypto_alt avg `-0.1283` n `235`; crypto_major avg `-0.0603` n `8`; equity avg `-0.0035` n `150`; fx avg `0.0178` n `6`; index avg `0.0023` n `26`; metal avg `0.0805` n `20`; unknown avg `0.1115` n `1076`
- 4h: commodity avg `-0.1075` n `13`; crypto_alt avg `-0.0111` n `235`; crypto_major avg `0.0273` n `8`; equity avg `0.036` n `150`; fx avg `0.046` n `6`; index avg `0.0185` n `26`; metal avg `0.2329` n `20`; unknown avg `0.3418` n `1069`
- 24h: commodity avg `0.4679` n `13`; crypto_alt avg `-4.0461` n `235`; crypto_major avg `-4.0891` n `8`; equity avg `-2.7608` n `150`; fx avg `0.1674` n `6`; index avg `-0.288` n `26`; metal avg `-0.0455` n `20`; unknown avg `6.0914` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
