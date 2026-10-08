# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T11:07:29.104693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `13`; crypto_alt avg `-0.2976` n `235`; crypto_major avg `-0.3314` n `8`; equity avg `-0.0911` n `150`; fx avg `-0.0185` n `6`; index avg `-0.0091` n `26`; metal avg `-0.07` n `20`; unknown avg `-0.2204` n `1075`
- 1h: commodity avg `0.1398` n `13`; crypto_alt avg `-0.9976` n `235`; crypto_major avg `-0.9403` n `8`; equity avg `-0.4608` n `150`; fx avg `0.0041` n `6`; index avg `-0.0736` n `26`; metal avg `-0.1349` n `20`; unknown avg `2.7295` n `1075`
- 4h: commodity avg `0.3467` n `13`; crypto_alt avg `-0.1838` n `235`; crypto_major avg `-0.758` n `8`; equity avg `-0.443` n `150`; fx avg `0.0599` n `6`; index avg `-0.0595` n `26`; metal avg `-0.151` n `20`; unknown avg `1.4932` n `1059`
- 24h: commodity avg `0.7481` n `13`; crypto_alt avg `-0.1742` n `235`; crypto_major avg `-2.1544` n `8`; equity avg `-1.5311` n `150`; fx avg `0.0189` n `6`; index avg `-0.272` n `26`; metal avg `-0.1637` n `20`; unknown avg `416.5824` n `974`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
