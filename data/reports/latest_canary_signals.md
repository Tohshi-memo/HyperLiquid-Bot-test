# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T03:52:30.803358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `-0.0947` n `237`; crypto_major avg `-0.07` n `8`; equity avg `-0.0087` n `151`; fx avg `0.0103` n `6`; index avg `-0.0024` n `26`; metal avg `-0.0084` n `20`; unknown avg `-0.0374` n `1194`
- 1h: commodity avg `-0.08` n `13`; crypto_alt avg `-0.3562` n `237`; crypto_major avg `-0.2135` n `8`; equity avg `0.1772` n `151`; fx avg `0.0385` n `6`; index avg `0.0516` n `26`; metal avg `0.0569` n `20`; unknown avg `2.5343` n `1192`
- 4h: commodity avg `-0.0926` n `13`; crypto_alt avg `0.321` n `237`; crypto_major avg `0.5317` n `8`; equity avg `1.5898` n `151`; fx avg `0.0074` n `6`; index avg `0.2798` n `26`; metal avg `0.1057` n `20`; unknown avg `1.3325` n `1128`
- 24h: commodity avg `-0.5034` n `13`; crypto_alt avg `-0.772` n `237`; crypto_major avg `0.3146` n `8`; equity avg `2.6684` n `151`; fx avg `0.0104` n `6`; index avg `0.5191` n `26`; metal avg `0.3136` n `20`; unknown avg `5.4171` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1988`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1455`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1155`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0818`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0684`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0639`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
