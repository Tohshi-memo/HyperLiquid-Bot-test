# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T04:07:22.972315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `13`; crypto_alt avg `-0.0345` n `238`; crypto_major avg `0.0518` n `8`; equity avg `0.011` n `156`; fx avg `-0.0017` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0003` n `20`; unknown avg `0.8232` n `1250`
- 1h: commodity avg `0.0431` n `13`; crypto_alt avg `-0.1632` n `238`; crypto_major avg `-0.2078` n `8`; equity avg `0.0079` n `156`; fx avg `0.0041` n `6`; index avg `-0.0283` n `27`; metal avg `0.0033` n `20`; unknown avg `-0.1272` n `1238`
- 4h: commodity avg `0.1084` n `13`; crypto_alt avg `-0.526` n `238`; crypto_major avg `-0.2879` n `8`; equity avg `-0.0083` n `156`; fx avg `0.0035` n `6`; index avg `-0.0409` n `27`; metal avg `-0.0033` n `20`; unknown avg `-0.2765` n `1232`
- 24h: commodity avg `0.0023` n `13`; crypto_alt avg `2.7131` n `238`; crypto_major avg `-0.6363` n `8`; equity avg `-2.3974` n `156`; fx avg `-0.0702` n `6`; index avg `-0.1444` n `27`; metal avg `-0.5758` n `20`; unknown avg `2.8396` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
