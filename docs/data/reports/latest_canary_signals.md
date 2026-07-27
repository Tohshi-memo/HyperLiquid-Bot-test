# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T17:22:35.096600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.8451` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0132` n `12`; crypto_alt avg `0.1302` n `230`; crypto_major avg `0.1821` n `8`; equity avg `-0.029` n `102`; fx avg `-0.0071` n `6`; index avg `0.0042` n `25`; metal avg `0.0131` n `20`; unknown avg `0.0945` n `774`
- 1h: commodity avg `-0.244` n `12`; crypto_alt avg `0.5852` n `230`; crypto_major avg `0.6652` n `8`; equity avg `0.0922` n `102`; fx avg `-0.0496` n `6`; index avg `-0.0332` n `25`; metal avg `-0.0838` n `20`; unknown avg `0.5152` n `774`
- 4h: commodity avg `-0.3668` n `12`; crypto_alt avg `-0.9732` n `230`; crypto_major avg `-0.6109` n `8`; equity avg `-2.456` n `102`; fx avg `-0.112` n `6`; index avg `-0.5977` n `25`; metal avg `-0.0557` n `20`; unknown avg `-0.3844` n `774`
- 24h: commodity avg `-0.7302` n `12`; crypto_alt avg `-0.9943` n `230`; crypto_major avg `-0.1421` n `8`; equity avg `-1.892` n `102`; fx avg `-0.0116` n `6`; index avg `-0.5437` n `25`; metal avg `0.1907` n `20`; unknown avg `-0.2494` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1929`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
