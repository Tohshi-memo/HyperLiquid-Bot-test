# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T07:52:29.382972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0606` n `12`; crypto_alt avg `-0.0784` n `234`; crypto_major avg `-0.0655` n `8`; equity avg `-0.0158` n `140`; fx avg `-0.0098` n `6`; index avg `-0.001` n `26`; metal avg `-0.0064` n `20`; unknown avg `0.5981` n `943`
- 1h: commodity avg `0.0709` n `12`; crypto_alt avg `-0.2941` n `234`; crypto_major avg `-0.083` n `8`; equity avg `0.0033` n `140`; fx avg `0.0087` n `6`; index avg `-0.0076` n `26`; metal avg `-0.0104` n `20`; unknown avg `0.6244` n `941`
- 4h: commodity avg `0.081` n `12`; crypto_alt avg `-0.5692` n `234`; crypto_major avg `-0.1932` n `8`; equity avg `-0.0793` n `140`; fx avg `0.0036` n `6`; index avg `-0.0193` n `26`; metal avg `-0.0062` n `20`; unknown avg `17.5365` n `895`
- 24h: commodity avg `0.2802` n `12`; crypto_alt avg `-0.4441` n `234`; crypto_major avg `-1.7337` n `8`; equity avg `-0.2237` n `140`; fx avg `-0.0554` n `6`; index avg `-0.0458` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.5912` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
