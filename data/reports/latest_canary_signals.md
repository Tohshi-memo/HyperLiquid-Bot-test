# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T12:52:31.031723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0067` n `13`; crypto_alt avg `0.1629` n `238`; crypto_major avg `0.0748` n `8`; equity avg `0.0266` n `156`; fx avg `-0.005` n `6`; index avg `0.0084` n `27`; metal avg `0.0037` n `20`; unknown avg `0.0187` n `1263`
- 1h: commodity avg `0.0158` n `13`; crypto_alt avg `0.0587` n `238`; crypto_major avg `-0.127` n `8`; equity avg `-0.051` n `156`; fx avg `0.0031` n `6`; index avg `0.0032` n `27`; metal avg `-0.0131` n `20`; unknown avg `0.183` n `1251`
- 4h: commodity avg `-0.0287` n `13`; crypto_alt avg `-0.1865` n `238`; crypto_major avg `-0.3314` n `8`; equity avg `0.0349` n `156`; fx avg `-0.0195` n `6`; index avg `0.0102` n `27`; metal avg `0.0187` n `20`; unknown avg `0.2001` n `1237`
- 24h: commodity avg `-0.0657` n `13`; crypto_alt avg `0.2017` n `238`; crypto_major avg `0.1269` n `8`; equity avg `0.5249` n `156`; fx avg `-0.0241` n `6`; index avg `0.04` n `27`; metal avg `0.0705` n `20`; unknown avg `1.3593` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
