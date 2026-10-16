# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T11:37:28.549898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `13`; crypto_alt avg `0.1878` n `236`; crypto_major avg `-0.016` n `8`; equity avg `-0.1429` n `151`; fx avg `0.0075` n `6`; index avg `-0.0343` n `26`; metal avg `-0.0302` n `20`; unknown avg `19.1818` n `1136`
- 1h: commodity avg `0.0903` n `13`; crypto_alt avg `0.4116` n `236`; crypto_major avg `0.5929` n `8`; equity avg `-0.251` n `151`; fx avg `0.0085` n `6`; index avg `-0.0427` n `26`; metal avg `-0.0208` n `20`; unknown avg `10.9984` n `1134`
- 4h: commodity avg `0.0399` n `13`; crypto_alt avg `0.5112` n `236`; crypto_major avg `0.7188` n `8`; equity avg `-0.4769` n `151`; fx avg `0.0632` n `6`; index avg `-0.0554` n `26`; metal avg `-0.0438` n `20`; unknown avg `1.9516` n `1066`
- 24h: commodity avg `0.0673` n `13`; crypto_alt avg `4.7663` n `236`; crypto_major avg `2.7509` n `8`; equity avg `2.0814` n `151`; fx avg `0.0272` n `6`; index avg `0.2587` n `26`; metal avg `0.242` n `20`; unknown avg `25.6479` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0959`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0921`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0908`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0828`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0736`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
