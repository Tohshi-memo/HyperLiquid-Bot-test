# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T04:07:26.401080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0348` n `13`; crypto_alt avg `-0.0851` n `237`; crypto_major avg `-0.118` n `8`; equity avg `-0.1413` n `151`; fx avg `-0.007` n `6`; index avg `-0.0305` n `26`; metal avg `-0.0313` n `20`; unknown avg `0.0282` n `1192`
- 1h: commodity avg `-0.0191` n `13`; crypto_alt avg `-0.0078` n `237`; crypto_major avg `-0.2012` n `8`; equity avg `-0.2273` n `151`; fx avg `-0.0559` n `6`; index avg `-0.0849` n `26`; metal avg `-0.028` n `20`; unknown avg `0.5579` n `1192`
- 4h: commodity avg `0.1386` n `13`; crypto_alt avg `0.1851` n `237`; crypto_major avg `-0.1382` n `8`; equity avg `-0.0692` n `151`; fx avg `-0.0126` n `6`; index avg `0.0099` n `26`; metal avg `-0.1468` n `20`; unknown avg `0.5936` n `1191`
- 24h: commodity avg `0.0701` n `13`; crypto_alt avg `2.1412` n `237`; crypto_major avg `1.3201` n `8`; equity avg `2.146` n `151`; fx avg `-0.0108` n `6`; index avg `0.3211` n `26`; metal avg `-0.1837` n `20`; unknown avg `212.2478` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
