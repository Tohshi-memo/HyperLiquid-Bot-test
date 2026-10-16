# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T11:07:31.360514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `-0.0217` n `236`; crypto_major avg `0.0865` n `8`; equity avg `-0.2013` n `151`; fx avg `-0.0094` n `6`; index avg `-0.0056` n `26`; metal avg `-0.0047` n `20`; unknown avg `0.4675` n `1134`
- 1h: commodity avg `0.0618` n `13`; crypto_alt avg `0.3353` n `236`; crypto_major avg `0.569` n `8`; equity avg `-0.1285` n `151`; fx avg `0.0343` n `6`; index avg `0.0199` n `26`; metal avg `0.0283` n `20`; unknown avg `1.8664` n `1134`
- 4h: commodity avg `0.0305` n `13`; crypto_alt avg `-0.1006` n `236`; crypto_major avg `0.2864` n `8`; equity avg `-0.4444` n `151`; fx avg `0.0566` n `6`; index avg `-0.027` n `26`; metal avg `-0.0078` n `20`; unknown avg `0.5104` n `1066`
- 24h: commodity avg `0.0612` n `13`; crypto_alt avg `4.6543` n `236`; crypto_major avg `2.6443` n `8`; equity avg `2.8208` n `151`; fx avg `0.0288` n `6`; index avg `0.3698` n `26`; metal avg `0.2811` n `20`; unknown avg `25.4019` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0976`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0921`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0833`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0757`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
