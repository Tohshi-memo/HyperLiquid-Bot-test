# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T02:37:24.401259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `-0.0254` n `230`; crypto_major avg `-0.0146` n `8`; equity avg `0.0228` n `92`; fx avg `-0.0007` n `6`; index avg `0.0009` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.0712` n `765`
- 1h: commodity avg `0.0573` n `12`; crypto_alt avg `0.1142` n `230`; crypto_major avg `0.0848` n `8`; equity avg `0.0403` n `92`; fx avg `0.0008` n `6`; index avg `0.0008` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.2821` n `765`
- 4h: commodity avg `0.3175` n `12`; crypto_alt avg `-0.8259` n `230`; crypto_major avg `-0.9343` n `8`; equity avg `-0.1817` n `92`; fx avg `0.0048` n `6`; index avg `-0.1186` n `25`; metal avg `-0.0461` n `20`; unknown avg `0.4172` n `765`
- 24h: commodity avg `0.5734` n `12`; crypto_alt avg `-0.6312` n `229`; crypto_major avg `-0.2887` n `8`; equity avg `0.0749` n `92`; fx avg `0.0212` n `6`; index avg `-0.0952` n `25`; metal avg `-0.0762` n `20`; unknown avg `-0.1415` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
