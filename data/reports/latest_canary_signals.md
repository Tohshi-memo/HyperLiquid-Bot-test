# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T14:37:26.464896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `13`; crypto_alt avg `0.014` n `238`; crypto_major avg `0.0286` n `8`; equity avg `0.0005` n `156`; fx avg `0.0071` n `6`; index avg `-0.001` n `27`; metal avg `-0.0043` n `20`; unknown avg `0.5868` n `1262`
- 1h: commodity avg `-0.0395` n `13`; crypto_alt avg `0.0814` n `238`; crypto_major avg `-0.1083` n `8`; equity avg `0.0748` n `156`; fx avg `0.0004` n `6`; index avg `0.0083` n `27`; metal avg `0.0068` n `20`; unknown avg `160.8492` n `1256`
- 4h: commodity avg `-0.0811` n `13`; crypto_alt avg `0.2555` n `238`; crypto_major avg `-0.1175` n `8`; equity avg `-0.0122` n `156`; fx avg `-0.0104` n `6`; index avg `-0.0081` n `27`; metal avg `0.0047` n `20`; unknown avg `15.637` n `1218`
- 24h: commodity avg `-0.3457` n `13`; crypto_alt avg `1.2716` n `238`; crypto_major avg `0.2871` n `8`; equity avg `-0.4582` n `156`; fx avg `0.0222` n `6`; index avg `-0.0985` n `27`; metal avg `-0.0785` n `20`; unknown avg `1.9611` n `1097`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
