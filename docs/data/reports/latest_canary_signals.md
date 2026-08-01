# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T02:07:31.663477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0957` n `12`; crypto_alt avg `0.0988` n `230`; crypto_major avg `0.0653` n `8`; equity avg `0.0759` n `102`; fx avg `-0.0157` n `6`; index avg `-0.0307` n `25`; metal avg `-0.0034` n `20`; unknown avg `0.0235` n `781`
- 1h: commodity avg `-0.088` n `12`; crypto_alt avg `0.0523` n `230`; crypto_major avg `0.0487` n `8`; equity avg `0.0305` n `102`; fx avg `-0.0141` n `6`; index avg `0.0432` n `25`; metal avg `0.0096` n `20`; unknown avg `-0.1752` n `781`
- 4h: commodity avg `-0.0377` n `12`; crypto_alt avg `0.7101` n `230`; crypto_major avg `0.2466` n `8`; equity avg `0.0836` n `102`; fx avg `-0.0212` n `6`; index avg `0.032` n `25`; metal avg `-0.0146` n `20`; unknown avg `4.0796` n `781`
- 24h: commodity avg `0.9953` n `12`; crypto_alt avg `-0.0274` n `230`; crypto_major avg `-1.7383` n `8`; equity avg `-2.1229` n `102`; fx avg `-0.1226` n `6`; index avg `-0.1937` n `25`; metal avg `-0.2454` n `20`; unknown avg `2.6798` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
