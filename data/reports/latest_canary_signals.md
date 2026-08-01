# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T19:52:24.567324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0376` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.062` n `12`; crypto_alt avg `0.1306` n `230`; crypto_major avg `0.0918` n `8`; equity avg `0.023` n `102`; fx avg `0.0019` n `6`; index avg `-0.0097` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0667` n `782`
- 1h: commodity avg `0.0507` n `12`; crypto_alt avg `0.443` n `230`; crypto_major avg `0.3574` n `8`; equity avg `-0.01` n `102`; fx avg `-0.0015` n `6`; index avg `-0.0013` n `25`; metal avg `0.0458` n `20`; unknown avg `0.1786` n `782`
- 4h: commodity avg `0.1161` n `12`; crypto_alt avg `-0.8925` n `230`; crypto_major avg `-1.0988` n `8`; equity avg `-0.2922` n `102`; fx avg `0.0125` n `6`; index avg `-0.0612` n `25`; metal avg `0.0111` n `20`; unknown avg `2.9673` n `782`
- 24h: commodity avg `0.5767` n `12`; crypto_alt avg `-0.6818` n `230`; crypto_major avg `-1.3087` n `8`; equity avg `-1.0575` n `102`; fx avg `-0.1681` n `6`; index avg `-0.1712` n `25`; metal avg `-0.0664` n `20`; unknown avg `4.334` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
