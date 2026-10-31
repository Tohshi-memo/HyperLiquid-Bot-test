# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T10:52:34.548435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `13`; crypto_alt avg `-0.0778` n `238`; crypto_major avg `-0.113` n `8`; equity avg `-0.0149` n `156`; fx avg `0.0015` n `6`; index avg `-0.0012` n `27`; metal avg `0.0035` n `20`; unknown avg `0.4491` n `1256`
- 1h: commodity avg `0.0422` n `13`; crypto_alt avg `0.0104` n `238`; crypto_major avg `0.1708` n `8`; equity avg `-0.0419` n `156`; fx avg `0.0166` n `6`; index avg `-0.0112` n `27`; metal avg `0.005` n `20`; unknown avg `-0.0007` n `1252`
- 4h: commodity avg `0.022` n `13`; crypto_alt avg `-0.4475` n `238`; crypto_major avg `-0.2572` n `8`; equity avg `-0.0906` n `156`; fx avg `0.0176` n `6`; index avg `-0.0112` n `27`; metal avg `-0.0023` n `20`; unknown avg `0.662` n `1232`
- 24h: commodity avg `-0.2969` n `13`; crypto_alt avg `0.1929` n `238`; crypto_major avg `-1.0836` n `8`; equity avg `-1.5427` n `156`; fx avg `-0.0999` n `6`; index avg `-0.1437` n `27`; metal avg `-0.3344` n `20`; unknown avg `4.5069` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
