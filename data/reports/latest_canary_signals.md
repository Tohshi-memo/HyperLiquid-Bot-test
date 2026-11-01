# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T12:07:23.125359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0116` n `13`; crypto_alt avg `0.0709` n `238`; crypto_major avg `0.0883` n `8`; equity avg `0.0179` n `156`; fx avg `0.0006` n `6`; index avg `0.0084` n `27`; metal avg `-0.0062` n `20`; unknown avg `-0.0438` n `1251`
- 1h: commodity avg `0.019` n `13`; crypto_alt avg `-0.0532` n `238`; crypto_major avg `0.0769` n `8`; equity avg `0.0625` n `156`; fx avg `-0.0053` n `6`; index avg `0.0065` n `27`; metal avg `0.0066` n `20`; unknown avg `-0.1301` n `1249`
- 4h: commodity avg `-0.0278` n `13`; crypto_alt avg `-0.0423` n `238`; crypto_major avg `0.221` n `8`; equity avg `0.1946` n `156`; fx avg `-0.0229` n `6`; index avg `0.0159` n `27`; metal avg `0.0169` n `20`; unknown avg `0.0353` n `1237`
- 24h: commodity avg `-0.0516` n `13`; crypto_alt avg `0.5891` n `238`; crypto_major avg `0.5046` n `8`; equity avg `0.5401` n `156`; fx avg `-0.0386` n `6`; index avg `0.038` n `27`; metal avg `0.0732` n `20`; unknown avg `1.3849` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
