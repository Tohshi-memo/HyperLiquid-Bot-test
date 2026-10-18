# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T10:52:24.257787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `-0.1462` n `237`; crypto_major avg `-0.1073` n `8`; equity avg `-0.0362` n `151`; fx avg `-0.0057` n `6`; index avg `-0.007` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.0191` n `1193`
- 1h: commodity avg `-0.0975` n `13`; crypto_alt avg `-0.4405` n `237`; crypto_major avg `-0.1461` n `8`; equity avg `-0.0443` n `151`; fx avg `-0.0104` n `6`; index avg `-0.0071` n `26`; metal avg `-0.0007` n `20`; unknown avg `3.8193` n `1191`
- 4h: commodity avg `-0.0096` n `13`; crypto_alt avg `-0.1167` n `237`; crypto_major avg `0.3146` n `8`; equity avg `0.2346` n `151`; fx avg `-0.0011` n `6`; index avg `0.052` n `26`; metal avg `0.0209` n `20`; unknown avg `5.0719` n `1079`
- 24h: commodity avg `0.0264` n `13`; crypto_alt avg `-2.4166` n `236`; crypto_major avg `-0.4933` n `8`; equity avg `-0.6663` n `151`; fx avg `-0.0531` n `6`; index avg `-0.068` n `26`; metal avg `-0.045` n `20`; unknown avg `4.6867` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2027`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1334`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1317`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1122`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0756`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
