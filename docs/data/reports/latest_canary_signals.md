# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T10:52:27.256314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `13`; crypto_alt avg `0.0753` n `239`; crypto_major avg `0.0663` n `8`; equity avg `0.0023` n `158`; fx avg `-0.016` n `6`; index avg `0.012` n `27`; metal avg `-0.0015` n `20`; unknown avg `0.3532` n `1261`
- 1h: commodity avg `0.0313` n `13`; crypto_alt avg `-0.2411` n `239`; crypto_major avg `-0.1175` n `8`; equity avg `-0.0431` n `158`; fx avg `-0.0049` n `6`; index avg `-0.0078` n `27`; metal avg `0.0058` n `20`; unknown avg `1.7229` n `1255`
- 4h: commodity avg `0.0818` n `13`; crypto_alt avg `-0.6675` n `239`; crypto_major avg `-0.2369` n `8`; equity avg `0.0908` n `158`; fx avg `-0.0071` n `6`; index avg `0.0103` n `27`; metal avg `-0.0006` n `20`; unknown avg `136.4066` n `1197`
- 24h: commodity avg `-0.1185` n `13`; crypto_alt avg `-1.1459` n `239`; crypto_major avg `-0.4307` n `8`; equity avg `-0.0824` n `158`; fx avg `-0.0045` n `6`; index avg `0.0054` n `27`; metal avg `0.1132` n `20`; unknown avg `7.7826` n `1049`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
