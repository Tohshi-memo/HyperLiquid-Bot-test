# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T00:22:31.286766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `13`; crypto_alt avg `-0.2498` n `235`; crypto_major avg `-0.1527` n `8`; equity avg `-0.0139` n `150`; fx avg `0.0055` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0222` n `20`; unknown avg `0.0727` n `1078`
- 1h: commodity avg `0.0675` n `13`; crypto_alt avg `-0.6513` n `235`; crypto_major avg `-0.4628` n `8`; equity avg `-0.0576` n `150`; fx avg `0.028` n `6`; index avg `0.0043` n `26`; metal avg `0.0418` n `20`; unknown avg `0.2373` n `1069`
- 4h: commodity avg `0.1081` n `13`; crypto_alt avg `-0.2118` n `235`; crypto_major avg `0.0404` n `8`; equity avg `0.0582` n `150`; fx avg `0.0349` n `6`; index avg `0.0172` n `26`; metal avg `0.1113` n `20`; unknown avg `0.2976` n `1061`
- 24h: commodity avg `0.5736` n `13`; crypto_alt avg `-3.7861` n `235`; crypto_major avg `-3.8476` n `8`; equity avg `-2.838` n `150`; fx avg `0.1634` n `6`; index avg `-0.3399` n `26`; metal avg `0.1435` n `20`; unknown avg `6.1284` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
