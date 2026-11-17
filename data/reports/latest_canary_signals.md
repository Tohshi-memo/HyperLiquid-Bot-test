# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T01:37:29.835989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0596` n `13`; crypto_alt avg `0.0878` n `239`; crypto_major avg `0.0082` n `8`; equity avg `-0.0056` n `162`; fx avg `-0.0069` n `6`; index avg `-0.011` n `27`; metal avg `0.077` n `20`; unknown avg `0.394` n `1266`
- 1h: commodity avg `-0.1017` n `13`; crypto_alt avg `0.0247` n `239`; crypto_major avg `0.2104` n `8`; equity avg `0.3895` n `162`; fx avg `0.0418` n `6`; index avg `0.0469` n `27`; metal avg `0.0671` n `20`; unknown avg `0.2153` n `1264`
- 4h: commodity avg `-0.0625` n `13`; crypto_alt avg `-0.5398` n `239`; crypto_major avg `-0.4276` n `8`; equity avg `0.0021` n `162`; fx avg `0.0567` n `6`; index avg `0.0113` n `27`; metal avg `0.0796` n `20`; unknown avg `0.6716` n `1220`
- 24h: commodity avg `-0.9822` n `13`; crypto_alt avg `0.2603` n `239`; crypto_major avg `0.5612` n `8`; equity avg `-2.8124` n `162`; fx avg `-0.0608` n `6`; index avg `-0.2801` n `27`; metal avg `-0.1883` n `20`; unknown avg `514.1575` n `997`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
