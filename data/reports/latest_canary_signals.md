# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T03:52:33.713150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `13`; crypto_alt avg `-0.061` n `235`; crypto_major avg `-0.0003` n `8`; equity avg `0.0124` n `143`; fx avg `0.0045` n `6`; index avg `-0.0011` n `26`; metal avg `0.0021` n `20`; unknown avg `0.2339` n `1079`
- 1h: commodity avg `-0.0544` n `13`; crypto_alt avg `0.0981` n `235`; crypto_major avg `0.1238` n `8`; equity avg `0.0304` n `143`; fx avg `0.005` n `6`; index avg `0.0011` n `26`; metal avg `0.0095` n `20`; unknown avg `-0.0601` n `1077`
- 4h: commodity avg `-0.041` n `13`; crypto_alt avg `-0.078` n `235`; crypto_major avg `0.2266` n `8`; equity avg `0.0211` n `143`; fx avg `0.0022` n `6`; index avg `-0.0085` n `26`; metal avg `0.0147` n `20`; unknown avg `-0.1123` n `1071`
- 24h: commodity avg `0.1109` n `13`; crypto_alt avg `1.1157` n `235`; crypto_major avg `0.6433` n `8`; equity avg `0.2049` n `143`; fx avg `-0.0233` n `6`; index avg `0.0081` n `26`; metal avg `0.0029` n `20`; unknown avg `0.1472` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2019`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1852`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
