# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T03:37:37.352336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0281` n `13`; crypto_alt avg `-0.0446` n `235`; crypto_major avg `0.0294` n `8`; equity avg `0.0703` n `150`; fx avg `-0.0009` n `6`; index avg `0.0105` n `26`; metal avg `-0.0038` n `20`; unknown avg `4.4779` n `1078`
- 1h: commodity avg `-0.0269` n `13`; crypto_alt avg `0.7894` n `235`; crypto_major avg `0.4641` n `8`; equity avg `0.0139` n `150`; fx avg `-0.001` n `6`; index avg `0.0097` n `26`; metal avg `-0.0036` n `20`; unknown avg `1.2274` n `1076`
- 4h: commodity avg `-0.1352` n `13`; crypto_alt avg `0.8802` n `235`; crypto_major avg `0.4573` n `8`; equity avg `0.4514` n `150`; fx avg `0.0193` n `6`; index avg `0.092` n `26`; metal avg `0.3356` n `20`; unknown avg `1.2592` n `1069`
- 24h: commodity avg `0.1603` n `13`; crypto_alt avg `-2.0384` n `235`; crypto_major avg `-2.6892` n `8`; equity avg `-1.9516` n `150`; fx avg `0.0994` n `6`; index avg `-0.1897` n `26`; metal avg `0.0908` n `20`; unknown avg `6.2695` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
