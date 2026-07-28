# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T03:22:33.774196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0973` n `12`; crypto_alt avg `0.0295` n `230`; crypto_major avg `0.1647` n `8`; equity avg `0.3544` n `102`; fx avg `-0.0122` n `6`; index avg `0.0925` n `25`; metal avg `0.0429` n `20`; unknown avg `-0.022` n `774`
- 1h: commodity avg `-0.0171` n `12`; crypto_alt avg `-0.0446` n `230`; crypto_major avg `-0.0731` n `8`; equity avg `-0.1755` n `102`; fx avg `-0.0317` n `6`; index avg `-0.036` n `25`; metal avg `-0.0115` n `20`; unknown avg `-0.0966` n `774`
- 4h: commodity avg `-0.1932` n `12`; crypto_alt avg `-0.5341` n `230`; crypto_major avg `-0.6781` n `8`; equity avg `-1.3137` n `102`; fx avg `-0.0007` n `6`; index avg `-0.2883` n `25`; metal avg `-0.27` n `20`; unknown avg `0.3139` n `774`
- 24h: commodity avg `-0.9077` n `12`; crypto_alt avg `-3.8753` n `230`; crypto_major avg `-3.166` n `8`; equity avg `-3.2387` n `102`; fx avg `-0.1295` n `6`; index avg `-0.7109` n `25`; metal avg `-0.2826` n `20`; unknown avg `1161.8575` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
