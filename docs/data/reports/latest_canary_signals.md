# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T12:22:25.906868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.18` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0174` n `13`; crypto_alt avg `-0.3706` n `238`; crypto_major avg `-0.3943` n `8`; equity avg `-0.1114` n `156`; fx avg `0.0015` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0174` n `20`; unknown avg `0.9551` n `1263`
- 1h: commodity avg `0.0353` n `13`; crypto_alt avg `-0.4165` n `238`; crypto_major avg `-0.3417` n `8`; equity avg `-0.0567` n `156`; fx avg `-0.0094` n `6`; index avg `-0.0041` n `27`; metal avg `-0.0135` n `20`; unknown avg `0.3152` n `1251`
- 4h: commodity avg `-0.0104` n `13`; crypto_alt avg `-0.318` n `238`; crypto_major avg `-0.0486` n `8`; equity avg `0.0942` n `156`; fx avg `-0.0154` n `6`; index avg `0.0074` n `27`; metal avg `0.0128` n `20`; unknown avg `0.2508` n `1237`
- 24h: commodity avg `-0.0436` n `13`; crypto_alt avg `0.0485` n `238`; crypto_major avg `0.0048` n `8`; equity avg `0.4522` n `156`; fx avg `-0.0302` n `6`; index avg `0.0295` n `27`; metal avg `0.0614` n `20`; unknown avg `1.3795` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
