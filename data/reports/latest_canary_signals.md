# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T17:23:02.696540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1964` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0324` n `12`; crypto_alt avg `-0.0013` n `232`; crypto_major avg `0.0167` n `8`; equity avg `0.004` n `134`; fx avg `0.0037` n `6`; index avg `0.0054` n `26`; metal avg `-0.0048` n `20`; unknown avg `0.2835` n `796`
- 1h: commodity avg `0.0113` n `12`; crypto_alt avg `0.5207` n `232`; crypto_major avg `0.4437` n `8`; equity avg `0.1722` n `134`; fx avg `-0.0004` n `6`; index avg `0.0337` n `26`; metal avg `-0.0114` n `20`; unknown avg `1.1191` n `788`
- 4h: commodity avg `0.0038` n `12`; crypto_alt avg `-1.116` n `232`; crypto_major avg `-1.1538` n `8`; equity avg `0.0348` n `134`; fx avg `-0.0305` n `6`; index avg `0.0426` n `26`; metal avg `0.1326` n `20`; unknown avg `0.2206` n `788`
- 24h: commodity avg `0.1294` n `12`; crypto_alt avg `0.5013` n `232`; crypto_major avg `-0.77` n `8`; equity avg `0.5156` n `134`; fx avg `-0.1012` n `6`; index avg `0.0939` n `26`; metal avg `0.0224` n `20`; unknown avg `1.8508` n `681`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
