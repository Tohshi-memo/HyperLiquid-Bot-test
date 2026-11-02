# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T08:52:37.786297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0441` n `13`; crypto_alt avg `0.0002` n `238`; crypto_major avg `0.1162` n `8`; equity avg `0.057` n `156`; fx avg `0.0272` n `6`; index avg `0.0181` n `27`; metal avg `0.0857` n `20`; unknown avg `-0.0353` n `1262`
- 1h: commodity avg `-0.1117` n `13`; crypto_alt avg `0.0765` n `238`; crypto_major avg `0.4798` n `8`; equity avg `0.1201` n `156`; fx avg `0.0244` n `6`; index avg `0.0026` n `27`; metal avg `0.0479` n `20`; unknown avg `7.7377` n `1196`
- 4h: commodity avg `-0.1742` n `13`; crypto_alt avg `-0.979` n `238`; crypto_major avg `-0.3442` n `8`; equity avg `-0.2648` n `156`; fx avg `0.0669` n `6`; index avg `-0.0395` n `27`; metal avg `0.1524` n `20`; unknown avg `2.6258` n `1153`
- 24h: commodity avg `-0.5576` n `13`; crypto_alt avg `-1.9626` n `238`; crypto_major avg `-0.3563` n `8`; equity avg `0.9488` n `156`; fx avg `0.2678` n `6`; index avg `0.2967` n `27`; metal avg `0.1784` n `20`; unknown avg `2.6416` n `1063`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
