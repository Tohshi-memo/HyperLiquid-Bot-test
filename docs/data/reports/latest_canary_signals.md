# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T11:37:33.274683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `0.029` n `230`; crypto_major avg `0.0084` n `8`; equity avg `-0.0235` n `102`; fx avg `-0.0801` n `6`; index avg `-0.0535` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.0028` n `781`
- 1h: commodity avg `0.0317` n `12`; crypto_alt avg `0.0849` n `230`; crypto_major avg `0.0234` n `8`; equity avg `0.096` n `102`; fx avg `-0.1344` n `6`; index avg `-0.0293` n `25`; metal avg `-0.0105` n `20`; unknown avg `-0.0074` n `781`
- 4h: commodity avg `0.0783` n `12`; crypto_alt avg `-0.1478` n `230`; crypto_major avg `-0.1359` n `8`; equity avg `0.0885` n `102`; fx avg `-0.1295` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0424` n `20`; unknown avg `-0.0952` n `781`
- 24h: commodity avg `0.391` n `12`; crypto_alt avg `0.3446` n `230`; crypto_major avg `-1.2509` n `8`; equity avg `-2.5995` n `102`; fx avg `-0.2314` n `6`; index avg `-0.2769` n `25`; metal avg `-0.0005` n `20`; unknown avg `4.5877` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
