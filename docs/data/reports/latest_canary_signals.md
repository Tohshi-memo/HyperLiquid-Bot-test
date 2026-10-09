# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T02:52:26.430313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0466` n `13`; crypto_alt avg `0.4819` n `235`; crypto_major avg `0.4533` n `8`; equity avg `0.0419` n `150`; fx avg `0.0038` n `6`; index avg `0.0064` n `26`; metal avg `0.0061` n `20`; unknown avg `-0.1318` n `1078`
- 1h: commodity avg `0.0238` n `13`; crypto_alt avg `0.1242` n `235`; crypto_major avg `0.3528` n `8`; equity avg `-0.0835` n `150`; fx avg `0.0189` n `6`; index avg `0.0084` n `26`; metal avg `0.0273` n `20`; unknown avg `0.35` n `1076`
- 4h: commodity avg `-0.0477` n `13`; crypto_alt avg `0.6838` n `235`; crypto_major avg `0.5147` n `8`; equity avg `0.3313` n `150`; fx avg `0.0399` n `6`; index avg `0.0681` n `26`; metal avg `0.3948` n `20`; unknown avg `0.823` n `1069`
- 24h: commodity avg `0.2487` n `13`; crypto_alt avg `-2.7568` n `235`; crypto_major avg `-3.0837` n `8`; equity avg `-2.3257` n `150`; fx avg `0.1118` n `6`; index avg `-0.2665` n `26`; metal avg `0.0367` n `20`; unknown avg `6.7388` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
