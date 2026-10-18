# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T18:52:27.076807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `13`; crypto_alt avg `0.0833` n `237`; crypto_major avg `0.1671` n `8`; equity avg `0.0242` n `151`; fx avg `-0.0036` n `6`; index avg `-0.0018` n `26`; metal avg `0.0071` n `20`; unknown avg `1.6755` n `1194`
- 1h: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.0154` n `237`; crypto_major avg `0.0684` n `8`; equity avg `0.0258` n `151`; fx avg `0.0097` n `6`; index avg `-0.0145` n `26`; metal avg `0.0126` n `20`; unknown avg `2.2139` n `1182`
- 4h: commodity avg `0.0086` n `13`; crypto_alt avg `-0.4598` n `237`; crypto_major avg `-0.047` n `8`; equity avg `-0.1656` n `151`; fx avg `0.0109` n `6`; index avg `-0.0449` n `26`; metal avg `0.0075` n `20`; unknown avg `-0.9309` n `1151`
- 24h: commodity avg `-0.0278` n `13`; crypto_alt avg `-3.5936` n `236`; crypto_major avg `-1.3866` n `8`; equity avg `-1.0769` n `151`; fx avg `0.0017` n `6`; index avg `-0.1597` n `26`; metal avg `-0.0397` n `20`; unknown avg `0.4409` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2107`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1407`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1329`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1111`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
