# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T12:37:28.935962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `72.0` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.197` n `238`; crypto_major avg `0.1054` n `8`; equity avg `0.0161` n `156`; fx avg `0.006` n `6`; index avg `-0.0043` n `27`; metal avg `0.0067` n `20`; unknown avg `0.5752` n `1263`
- 1h: commodity avg `0.0269` n `13`; crypto_alt avg `-0.167` n `238`; crypto_major avg `-0.1765` n `8`; equity avg `-0.0194` n `156`; fx avg `-0.0009` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0178` n `20`; unknown avg `0.7673` n `1251`
- 4h: commodity avg `-0.0189` n `13`; crypto_alt avg `-0.2728` n `238`; crypto_major avg `-0.1761` n `8`; equity avg `0.0198` n `156`; fx avg `-0.0116` n `6`; index avg `-0.0006` n `27`; metal avg `0.0129` n `20`; unknown avg `0.8435` n `1237`
- 24h: commodity avg `-0.0471` n `13`; crypto_alt avg `0.0222` n `238`; crypto_major avg `-0.0535` n `8`; equity avg `0.4548` n `156`; fx avg `-0.0239` n `6`; index avg `0.0256` n `27`; metal avg `0.06` n `20`; unknown avg `1.3827` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
