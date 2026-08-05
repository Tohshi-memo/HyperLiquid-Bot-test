# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T00:37:25.788840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `12`; crypto_alt avg `0.1406` n `230`; crypto_major avg `0.227` n `8`; equity avg `0.2143` n `108`; fx avg `-0.0076` n `6`; index avg `0.0206` n `25`; metal avg `0.0496` n `20`; unknown avg `0.0006` n `781`
- 1h: commodity avg `0.0794` n `12`; crypto_alt avg `-0.0137` n `230`; crypto_major avg `0.0417` n `8`; equity avg `0.4938` n `108`; fx avg `-0.0395` n `6`; index avg `0.1047` n `25`; metal avg `0.0969` n `20`; unknown avg `-0.0888` n `781`
- 4h: commodity avg `0.0844` n `12`; crypto_alt avg `-0.0935` n `230`; crypto_major avg `-0.2728` n `8`; equity avg `1.0579` n `108`; fx avg `-0.0335` n `6`; index avg `0.1401` n `25`; metal avg `0.0611` n `20`; unknown avg `0.1105` n `781`
- 24h: commodity avg `-1.301` n `12`; crypto_alt avg `0.2981` n `230`; crypto_major avg `0.8801` n `8`; equity avg `4.3879` n `107`; fx avg `0.0766` n `6`; index avg `0.9243` n `25`; metal avg `0.885` n `20`; unknown avg `0.407` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
