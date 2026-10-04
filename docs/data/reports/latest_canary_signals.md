# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T08:07:28.924631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `13`; crypto_alt avg `0.0064` n `235`; crypto_major avg `0.1189` n `8`; equity avg `-0.0002` n `143`; fx avg `0.0012` n `6`; index avg `0.0005` n `26`; metal avg `0.0068` n `20`; unknown avg `-0.0658` n `1061`
- 1h: commodity avg `-0.0316` n `13`; crypto_alt avg `0.0458` n `235`; crypto_major avg `0.1281` n `8`; equity avg `-0.0251` n `143`; fx avg `0.0026` n `6`; index avg `-0.0078` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.0476` n `1061`
- 4h: commodity avg `0.0077` n `13`; crypto_alt avg `0.6514` n `235`; crypto_major avg `0.387` n `8`; equity avg `-0.0078` n `143`; fx avg `-0.018` n `6`; index avg `-0.0066` n `26`; metal avg `0.0044` n `20`; unknown avg `0.1294` n `1033`
- 24h: commodity avg `0.1199` n `13`; crypto_alt avg `2.654` n `235`; crypto_major avg `1.2248` n `8`; equity avg `0.2187` n `143`; fx avg `-0.041` n `6`; index avg `0.0161` n `26`; metal avg `0.0037` n `20`; unknown avg `0.2295` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
