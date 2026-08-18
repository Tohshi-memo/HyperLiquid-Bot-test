# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T11:37:28.027790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.057` n `12`; crypto_alt avg `-0.0254` n `230`; crypto_major avg `-0.0226` n `8`; equity avg `-0.1225` n `114`; fx avg `0.0036` n `6`; index avg `-0.014` n `25`; metal avg `-0.0367` n `20`; unknown avg `0.0062` n `795`
- 1h: commodity avg `0.0954` n `12`; crypto_alt avg `0.1735` n `230`; crypto_major avg `0.2546` n `8`; equity avg `0.2511` n `114`; fx avg `-0.0053` n `6`; index avg `0.0373` n `25`; metal avg `-0.0315` n `20`; unknown avg `0.0211` n `795`
- 4h: commodity avg `0.0518` n `12`; crypto_alt avg `0.2956` n `230`; crypto_major avg `0.106` n `8`; equity avg `-0.7666` n `114`; fx avg `-0.0277` n `6`; index avg `-0.0792` n `25`; metal avg `-0.0736` n `20`; unknown avg `-0.0139` n `795`
- 24h: commodity avg `0.6623` n `12`; crypto_alt avg `-0.7783` n `230`; crypto_major avg `0.1393` n `8`; equity avg `-2.4238` n `114`; fx avg `-0.0391` n `6`; index avg `-0.5073` n `25`; metal avg `-0.2742` n `20`; unknown avg `-0.018` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
