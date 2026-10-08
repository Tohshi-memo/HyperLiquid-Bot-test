# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T22:37:32.469224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1061` n `13`; crypto_alt avg `0.0948` n `235`; crypto_major avg `0.0401` n `8`; equity avg `0.0466` n `150`; fx avg `-0.0004` n `6`; index avg `0.0123` n `26`; metal avg `0.0151` n `20`; unknown avg `0.0557` n `1077`
- 1h: commodity avg `-0.1373` n `13`; crypto_alt avg `0.1868` n `235`; crypto_major avg `0.0873` n `8`; equity avg `0.1944` n `150`; fx avg `0.0008` n `6`; index avg `0.0427` n `26`; metal avg `0.045` n `20`; unknown avg `0.1215` n `1075`
- 4h: commodity avg `-0.2919` n `13`; crypto_alt avg `1.5595` n `235`; crypto_major avg `1.2914` n `8`; equity avg `0.5393` n `150`; fx avg `0.0249` n `6`; index avg `0.0935` n `26`; metal avg `0.1017` n `20`; unknown avg `0.3011` n `1007`
- 24h: commodity avg `0.424` n `13`; crypto_alt avg `-2.7106` n `235`; crypto_major avg `-3.2462` n `8`; equity avg `-2.6087` n `150`; fx avg `0.0601` n `6`; index avg `-0.3335` n `26`; metal avg `0.0648` n `20`; unknown avg `6.1843` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
