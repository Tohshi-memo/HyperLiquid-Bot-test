# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T04:22:32.529625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `13`; crypto_alt avg `-0.1249` n `237`; crypto_major avg `0.0235` n `8`; equity avg `-0.0615` n `151`; fx avg `0.0006` n `6`; index avg `-0.011` n `26`; metal avg `-0.0265` n `20`; unknown avg `-0.0354` n `1194`
- 1h: commodity avg `-0.0496` n `13`; crypto_alt avg `-0.3016` n `237`; crypto_major avg `-0.0513` n `8`; equity avg `-0.0868` n `151`; fx avg `0.0033` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0107` n `20`; unknown avg `3.4162` n `1186`
- 4h: commodity avg `-0.0179` n `13`; crypto_alt avg `0.2194` n `237`; crypto_major avg `0.5566` n `8`; equity avg `0.9737` n `151`; fx avg `-0.0177` n `6`; index avg `0.1672` n `26`; metal avg `0.1013` n `20`; unknown avg `0.8009` n `1130`
- 24h: commodity avg `-0.4377` n `13`; crypto_alt avg `-0.6102` n `237`; crypto_major avg `0.5058` n `8`; equity avg `2.6945` n `151`; fx avg `-0.0053` n `6`; index avg `0.5092` n `26`; metal avg `0.2982` n `20`; unknown avg `4.1347` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1973`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1438`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1189`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0758`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0719`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
