# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T00:52:32.797592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `-0.1758` n `230`; crypto_major avg `-0.2442` n `8`; equity avg `-0.2587` n `108`; fx avg `-0.0409` n `6`; index avg `-0.0401` n `25`; metal avg `-0.0197` n `20`; unknown avg `0.0421` n `781`
- 1h: commodity avg `0.0797` n `12`; crypto_alt avg `-0.1235` n `230`; crypto_major avg `-0.2098` n `8`; equity avg `0.1013` n `108`; fx avg `-0.0756` n `6`; index avg `0.0524` n `25`; metal avg `0.0484` n `20`; unknown avg `0.0162` n `781`
- 4h: commodity avg `0.0596` n `12`; crypto_alt avg `-0.401` n `230`; crypto_major avg `-0.5745` n `8`; equity avg `0.5559` n `108`; fx avg `-0.0758` n `6`; index avg `0.0803` n `25`; metal avg `0.0265` n `20`; unknown avg `0.3236` n `781`
- 24h: commodity avg `-1.3851` n `12`; crypto_alt avg `0.2728` n `230`; crypto_major avg `0.7055` n `8`; equity avg `4.1516` n `107`; fx avg `0.0862` n `6`; index avg `0.918` n `25`; metal avg `0.9241` n `20`; unknown avg `0.4183` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
