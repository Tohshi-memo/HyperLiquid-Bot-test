# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T03:22:27.636798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `13`; crypto_alt avg `0.1631` n `238`; crypto_major avg `0.0266` n `8`; equity avg `0.0226` n `156`; fx avg `-0.0069` n `6`; index avg `-0.0001` n `27`; metal avg `0.0019` n `20`; unknown avg `0.0654` n `1260`
- 1h: commodity avg `0.0469` n `13`; crypto_alt avg `0.2049` n `238`; crypto_major avg `0.0027` n `8`; equity avg `0.0576` n `156`; fx avg `0.0007` n `6`; index avg `0.019` n `27`; metal avg `-0.0037` n `20`; unknown avg `0.655` n `1252`
- 4h: commodity avg `0.0343` n `13`; crypto_alt avg `0.0867` n `238`; crypto_major avg `0.1785` n `8`; equity avg `0.0849` n `156`; fx avg `0.0023` n `6`; index avg `-0.0077` n `27`; metal avg `0.006` n `20`; unknown avg `0.8638` n `1200`
- 24h: commodity avg `-0.059` n `13`; crypto_alt avg `-0.47` n `238`; crypto_major avg `-0.3233` n `8`; equity avg `0.0647` n `156`; fx avg `0.0112` n `6`; index avg `-0.0348` n `27`; metal avg `0.0545` n `20`; unknown avg `1.8594` n `1002`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
