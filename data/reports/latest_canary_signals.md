# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T00:22:32.614343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0306` n `13`; crypto_alt avg `-0.1364` n `236`; crypto_major avg `0.0766` n `8`; equity avg `-0.1834` n `151`; fx avg `0.0504` n `6`; index avg `-0.086` n `26`; metal avg `0.12` n `20`; unknown avg `-0.1131` n `1136`
- 1h: commodity avg `-0.0216` n `13`; crypto_alt avg `-0.0361` n `236`; crypto_major avg `0.1832` n `8`; equity avg `0.0066` n `151`; fx avg `0.096` n `6`; index avg `-0.148` n `26`; metal avg `0.1698` n `20`; unknown avg `0.0691` n `1128`
- 4h: commodity avg `-0.052` n `13`; crypto_alt avg `0.0135` n `236`; crypto_major avg `-0.0552` n `8`; equity avg `-1.3668` n `151`; fx avg `0.1226` n `6`; index avg `-0.2897` n `26`; metal avg `0.1866` n `20`; unknown avg `0.5204` n `1018`
- 24h: commodity avg `-0.2374` n `13`; crypto_alt avg `-2.5437` n `236`; crypto_major avg `-2.0037` n `8`; equity avg `-5.6089` n `151`; fx avg `0.0279` n `6`; index avg `-0.8613` n `26`; metal avg `-0.6446` n `20`; unknown avg `1392.2138` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1017`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0916`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0806`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0676`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
