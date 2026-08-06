# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T06:07:28.845922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0636` n `12`; crypto_alt avg `0.0765` n `230`; crypto_major avg `-0.0646` n `8`; equity avg `-0.0263` n `108`; fx avg `0.0122` n `6`; index avg `0.0199` n `25`; metal avg `-0.017` n `20`; unknown avg `-0.0071` n `750`
- 1h: commodity avg `0.0694` n `12`; crypto_alt avg `-0.0716` n `230`; crypto_major avg `-0.1098` n `8`; equity avg `-0.2968` n `108`; fx avg `-0.0008` n `6`; index avg `-0.0638` n `25`; metal avg `0.0293` n `20`; unknown avg `-0.0237` n `750`
- 4h: commodity avg `-0.0725` n `12`; crypto_alt avg `0.3064` n `230`; crypto_major avg `0.2174` n `8`; equity avg `0.1703` n `108`; fx avg `0.0434` n `6`; index avg `0.0249` n `25`; metal avg `-0.2579` n `20`; unknown avg `-0.057` n `750`
- 24h: commodity avg `-0.0396` n `12`; crypto_alt avg `0.0559` n `230`; crypto_major avg `-0.0468` n `8`; equity avg `-2.3159` n `108`; fx avg `-0.0188` n `6`; index avg `-0.4192` n `25`; metal avg `0.3143` n `20`; unknown avg `0.8234` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
