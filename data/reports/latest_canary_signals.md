# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T05:07:28.056053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `13`; crypto_alt avg `0.4381` n `236`; crypto_major avg `0.4693` n `8`; equity avg `0.1001` n `151`; fx avg `-0.0246` n `6`; index avg `0.017` n `26`; metal avg `-0.0211` n `20`; unknown avg `4.9009` n `1134`
- 1h: commodity avg `0.022` n `13`; crypto_alt avg `0.7023` n `236`; crypto_major avg `0.5599` n `8`; equity avg `0.1952` n `151`; fx avg `-0.024` n `6`; index avg `0.0152` n `26`; metal avg `-0.0647` n `20`; unknown avg `1.9571` n `1132`
- 4h: commodity avg `-0.0281` n `13`; crypto_alt avg `0.153` n `236`; crypto_major avg `0.2361` n `8`; equity avg `0.8752` n `151`; fx avg `-0.0136` n `6`; index avg `0.1203` n `26`; metal avg `0.2476` n `20`; unknown avg `0.1727` n `1124`
- 24h: commodity avg `0.0102` n `13`; crypto_alt avg `3.7335` n `236`; crypto_major avg `1.8986` n `8`; equity avg `2.3439` n `151`; fx avg `0.0124` n `6`; index avg `0.3528` n `26`; metal avg `0.4788` n `20`; unknown avg `25.4706` n `906`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1038`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0937`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0731`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.072`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0649`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
