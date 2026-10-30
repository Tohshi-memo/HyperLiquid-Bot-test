# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T10:52:30.433953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0558` n `13`; crypto_alt avg `-0.0085` n `238`; crypto_major avg `0.0039` n `8`; equity avg `-0.2046` n `156`; fx avg `0.0072` n `6`; index avg `-0.0203` n `27`; metal avg `-0.0501` n `20`; unknown avg `2980.9283` n `1261`
- 1h: commodity avg `0.0701` n `13`; crypto_alt avg `0.6302` n `238`; crypto_major avg `0.4981` n `8`; equity avg `-0.1486` n `156`; fx avg `0.0123` n `6`; index avg `-0.0335` n `27`; metal avg `-0.1125` n `20`; unknown avg `0.0591` n `1255`
- 4h: commodity avg `0.3513` n `13`; crypto_alt avg `0.1611` n `238`; crypto_major avg `-0.8343` n `8`; equity avg `-1.0701` n `156`; fx avg `0.0658` n `6`; index avg `-0.0794` n `27`; metal avg `-0.1484` n `20`; unknown avg `2.3549` n `1192`
- 24h: commodity avg `0.3309` n `13`; crypto_alt avg `-3.856` n `238`; crypto_major avg `-1.8765` n `8`; equity avg `-3.9801` n `156`; fx avg `0.1011` n `6`; index avg `-0.4763` n `27`; metal avg `-0.7621` n `20`; unknown avg `24.1666` n `1032`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
