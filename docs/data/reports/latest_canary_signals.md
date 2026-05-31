# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T20:22:18.040005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0814` n `12`; crypto_alt avg `0.145` n `228`; crypto_major avg `0.0498` n `8`; equity avg `-0.0122` n `69`; fx avg `-0.0086` n `6`; index avg `-0.0279` n `23`; metal avg `-0.0202` n `18`; unknown avg `0.2939` n `421`
- 1h: commodity avg `-0.1384` n `12`; crypto_alt avg `0.5814` n `228`; crypto_major avg `0.2437` n `8`; equity avg `-0.029` n `69`; fx avg `-0.01` n `6`; index avg `-0.144` n `23`; metal avg `-0.0405` n `18`; unknown avg `0.4045` n `421`
- 4h: commodity avg `-0.0678` n `12`; crypto_alt avg `0.57` n `228`; crypto_major avg `-0.0506` n `8`; equity avg `0.0386` n `69`; fx avg `-0.0059` n `6`; index avg `0.0961` n `23`; metal avg `-0.0241` n `18`; unknown avg `0.4055` n `421`
- 24h: commodity avg `0.5933` n `12`; crypto_alt avg `-0.9403` n `228`; crypto_major avg `-0.5551` n `8`; equity avg `0.7715` n `69`; fx avg `-0.0351` n `6`; index avg `0.1399` n `23`; metal avg `-0.1628` n `18`; unknown avg `0.5159` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2629`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
