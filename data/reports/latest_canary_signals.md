# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T05:22:28.245019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `13`; crypto_alt avg `-0.0018` n `237`; crypto_major avg `0.0128` n `8`; equity avg `-0.0746` n `151`; fx avg `-0.0166` n `6`; index avg `-0.0138` n `26`; metal avg `-0.0315` n `20`; unknown avg `10.8118` n `1194`
- 1h: commodity avg `-0.0056` n `13`; crypto_alt avg `0.0764` n `237`; crypto_major avg `0.0844` n `8`; equity avg `-0.0449` n `151`; fx avg `-0.0258` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0165` n `20`; unknown avg `7.1875` n `1190`
- 4h: commodity avg `-0.1129` n `13`; crypto_alt avg `-0.1215` n `237`; crypto_major avg `0.2302` n `8`; equity avg `0.4045` n `151`; fx avg `-0.0553` n `6`; index avg `0.0596` n `26`; metal avg `0.0978` n `20`; unknown avg `3.0081` n `1184`
- 24h: commodity avg `-0.4109` n `13`; crypto_alt avg `-0.0292` n `237`; crypto_major avg `0.8488` n `8`; equity avg `2.6213` n `151`; fx avg `-0.0363` n `6`; index avg `0.4987` n `26`; metal avg `0.2801` n `20`; unknown avg `3.5905` n `901`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1983`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0978`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0727`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0719`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0676`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
