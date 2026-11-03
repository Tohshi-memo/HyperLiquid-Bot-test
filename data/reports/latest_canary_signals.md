# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T15:07:39.695270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.2372` n `239`; crypto_major avg `-0.1839` n `8`; equity avg `-0.0878` n `157`; fx avg `0.0101` n `6`; index avg `0.0057` n `27`; metal avg `-0.0367` n `20`; unknown avg `1.1208` n `1258`
- 1h: commodity avg `-0.0683` n `13`; crypto_alt avg `0.2453` n `239`; crypto_major avg `0.3147` n `8`; equity avg `0.5073` n `157`; fx avg `0.0485` n `6`; index avg `0.011` n `27`; metal avg `-0.0825` n `20`; unknown avg `1.3119` n `1258`
- 4h: commodity avg `-0.6008` n `13`; crypto_alt avg `0.8183` n `239`; crypto_major avg `0.7177` n `8`; equity avg `1.0686` n `157`; fx avg `0.0436` n `6`; index avg `0.1174` n `27`; metal avg `0.2836` n `20`; unknown avg `5.4754` n `1240`
- 24h: commodity avg `-0.3909` n `13`; crypto_alt avg `-0.5541` n `239`; crypto_major avg `-0.0672` n `8`; equity avg `-1.0974` n `157`; fx avg `0.0466` n `6`; index avg `-0.0992` n `27`; metal avg `-0.4594` n `20`; unknown avg `0.0946` n `1020`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
