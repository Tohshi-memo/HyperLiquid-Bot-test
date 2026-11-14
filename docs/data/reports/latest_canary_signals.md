# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T10:07:26.941484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `-0.0815` n `239`; crypto_major avg `-0.1454` n `8`; equity avg `-0.0351` n `162`; fx avg `0.0027` n `6`; index avg `-0.0026` n `27`; metal avg `0.0085` n `20`; unknown avg `166.2616` n `1256`
- 1h: commodity avg `-0.0209` n `13`; crypto_alt avg `0.1493` n `239`; crypto_major avg `0.2937` n `8`; equity avg `0.0717` n `162`; fx avg `-0.0019` n `6`; index avg `0.012` n `27`; metal avg `0.02` n `20`; unknown avg `13.0107` n `1216`
- 4h: commodity avg `0.015` n `13`; crypto_alt avg `-0.8785` n `239`; crypto_major avg `-0.1794` n `8`; equity avg `-0.0012` n `162`; fx avg `-0.0082` n `6`; index avg `0.0002` n `27`; metal avg `0.0348` n `20`; unknown avg `15.787` n `1182`
- 24h: commodity avg `-0.0624` n `13`; crypto_alt avg `-2.5267` n `239`; crypto_major avg `-3.0211` n `8`; equity avg `-2.7262` n `162`; fx avg `-0.1303` n `6`; index avg `-0.2243` n `27`; metal avg `-0.3749` n `20`; unknown avg `4.569` n `1044`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
