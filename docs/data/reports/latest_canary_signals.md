# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T16:46:28.763922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6146` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `-0.1753` n `230`; crypto_major avg `-0.2318` n `8`; equity avg `-0.1567` n `94`; fx avg `0.0072` n `6`; index avg `-0.0102` n `25`; metal avg `-0.0274` n `20`; unknown avg `-0.0794` n `768`
- 1h: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.2865` n `230`; crypto_major avg `-0.6297` n `8`; equity avg `-0.5647` n `94`; fx avg `-0.0216` n `6`; index avg `-0.1332` n `25`; metal avg `-0.1736` n `20`; unknown avg `-0.1641` n `768`
- 4h: commodity avg `-0.4599` n `12`; crypto_alt avg `0.4791` n `230`; crypto_major avg `0.0762` n `8`; equity avg `-1.5384` n `94`; fx avg `-0.0559` n `6`; index avg `-0.022` n `25`; metal avg `-0.0105` n `20`; unknown avg `-0.176` n `768`
- 24h: commodity avg `-0.1929` n `12`; crypto_alt avg `-0.3693` n `230`; crypto_major avg `-1.4049` n `8`; equity avg `-2.6445` n `94`; fx avg `-0.1183` n `6`; index avg `-0.2384` n `25`; metal avg `-0.2278` n `20`; unknown avg `-0.229` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
