# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T13:37:39.686234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0566` n `12`; crypto_alt avg `-0.3882` n `230`; crypto_major avg `-0.4196` n `8`; equity avg `-1.4332` n `102`; fx avg `0.0005` n `6`; index avg `-0.1127` n `25`; metal avg `-0.1643` n `20`; unknown avg `0.06` n `774`
- 1h: commodity avg `-0.0411` n `12`; crypto_alt avg `-0.4476` n `230`; crypto_major avg `-0.3416` n `8`; equity avg `-1.3374` n `102`; fx avg `0.0131` n `6`; index avg `-0.0826` n `25`; metal avg `-0.1245` n `20`; unknown avg `0.1049` n `774`
- 4h: commodity avg `0.0136` n `12`; crypto_alt avg `-0.539` n `230`; crypto_major avg `-0.6905` n `8`; equity avg `-1.9196` n `102`; fx avg `-0.0127` n `6`; index avg `-0.0713` n `25`; metal avg `-0.1305` n `20`; unknown avg `0.0294` n `774`
- 24h: commodity avg `-0.7711` n `12`; crypto_alt avg `-3.9948` n `230`; crypto_major avg `-4.3615` n `8`; equity avg `-5.5413` n `102`; fx avg `-0.1506` n `6`; index avg `-0.8513` n `25`; metal avg `-0.595` n `20`; unknown avg `1225.2076` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
