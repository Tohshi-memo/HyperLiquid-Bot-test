# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T15:22:33.561987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `-0.1028` n `230`; crypto_major avg `-0.0773` n `8`; equity avg `-0.0077` n `102`; fx avg `0.0055` n `6`; index avg `0.0081` n `25`; metal avg `0.0206` n `20`; unknown avg `0.0442` n `782`
- 1h: commodity avg `0.0405` n `12`; crypto_alt avg `-0.1124` n `230`; crypto_major avg `-0.0101` n `8`; equity avg `-0.0251` n `102`; fx avg `0.012` n `6`; index avg `0.0004` n `25`; metal avg `0.0194` n `20`; unknown avg `-0.0292` n `782`
- 4h: commodity avg `-0.0236` n `12`; crypto_alt avg `0.0644` n `230`; crypto_major avg `0.1551` n `8`; equity avg `-0.1936` n `102`; fx avg `0.0033` n `6`; index avg `-0.0554` n `25`; metal avg `0.0297` n `20`; unknown avg `-0.119` n `781`
- 24h: commodity avg `0.4383` n `12`; crypto_alt avg `0.5259` n `230`; crypto_major avg `-0.1576` n `8`; equity avg `-0.2662` n `102`; fx avg `-0.0314` n `6`; index avg `0.0398` n `25`; metal avg `0.0325` n `20`; unknown avg `4.2817` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
