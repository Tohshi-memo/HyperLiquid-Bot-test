# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T02:37:30.641059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0132` n `13`; crypto_alt avg `-0.1179` n `238`; crypto_major avg `-0.1381` n `8`; equity avg `-0.009` n `156`; fx avg `0.0001` n `6`; index avg `-0.0036` n `27`; metal avg `-0.0035` n `20`; unknown avg `0.085` n `1258`
- 1h: commodity avg `-0.0421` n `13`; crypto_alt avg `-0.4463` n `238`; crypto_major avg `-0.322` n `8`; equity avg `-0.0427` n `156`; fx avg `-0.0038` n `6`; index avg `-0.0` n `27`; metal avg `-0.0009` n `20`; unknown avg `0.1225` n `1252`
- 4h: commodity avg `-0.0357` n `13`; crypto_alt avg `-0.3433` n `238`; crypto_major avg `-0.2126` n `8`; equity avg `-0.0254` n `156`; fx avg `0.0028` n `6`; index avg `-0.0261` n `27`; metal avg `-0.0007` n `20`; unknown avg `0.893` n `1198`
- 24h: commodity avg `-0.0687` n `13`; crypto_alt avg `-0.6592` n `238`; crypto_major avg `-0.4624` n `8`; equity avg `0.0258` n `156`; fx avg `0.0023` n `6`; index avg `-0.0772` n `27`; metal avg `0.0725` n `20`; unknown avg `1.7647` n `1004`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
