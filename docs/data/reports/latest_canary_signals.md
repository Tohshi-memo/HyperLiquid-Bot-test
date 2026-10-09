# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T02:22:29.608529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `13`; crypto_alt avg `-0.2612` n `235`; crypto_major avg `-0.1398` n `8`; equity avg `-0.0331` n `150`; fx avg `-0.0031` n `6`; index avg `0.005` n `26`; metal avg `0.0145` n `20`; unknown avg `0.1138` n `1078`
- 1h: commodity avg `-0.1071` n `13`; crypto_alt avg `0.4006` n `235`; crypto_major avg `0.3506` n `8`; equity avg `0.3902` n `150`; fx avg `0.0056` n `6`; index avg `0.0625` n `26`; metal avg `0.0885` n `20`; unknown avg `1.2485` n `1076`
- 4h: commodity avg `-0.1565` n `13`; crypto_alt avg `0.4668` n `235`; crypto_major avg `0.142` n `8`; equity avg `0.2844` n `150`; fx avg `0.0363` n `6`; index avg `0.0593` n `26`; metal avg `0.3848` n `20`; unknown avg `1.1418` n `1069`
- 24h: commodity avg `0.2425` n `13`; crypto_alt avg `-2.8241` n `235`; crypto_major avg `-3.3451` n `8`; equity avg `-2.3463` n `150`; fx avg `0.1245` n `6`; index avg `-0.2674` n `26`; metal avg `0.0317` n `20`; unknown avg `6.1872` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
