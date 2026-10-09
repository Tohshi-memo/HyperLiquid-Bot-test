# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T00:07:31.599447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0281` n `13`; crypto_alt avg `0.1623` n `235`; crypto_major avg `0.1044` n `8`; equity avg `0.1694` n `150`; fx avg `-0.0016` n `6`; index avg `0.0303` n `26`; metal avg `0.0394` n `20`; unknown avg `-0.0105` n `1069`
- 1h: commodity avg `0.1127` n `13`; crypto_alt avg `-0.1653` n `235`; crypto_major avg `-0.1775` n `8`; equity avg `-0.057` n `150`; fx avg `0.0248` n `6`; index avg `0.005` n `26`; metal avg `0.0974` n `20`; unknown avg `0.1595` n `1069`
- 4h: commodity avg `0.1328` n `13`; crypto_alt avg `0.2215` n `235`; crypto_major avg `0.1951` n `8`; equity avg `0.1447` n `150`; fx avg `0.0323` n `6`; index avg `0.0276` n `26`; metal avg `0.1429` n `20`; unknown avg `-0.2021` n `1015`
- 24h: commodity avg `0.5732` n `13`; crypto_alt avg `-3.2798` n `235`; crypto_major avg `-3.6213` n `8`; equity avg `-2.8385` n `150`; fx avg `0.1245` n `6`; index avg `-0.3437` n `26`; metal avg `0.1547` n `20`; unknown avg `6.43` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
