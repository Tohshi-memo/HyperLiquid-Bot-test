# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T05:37:27.077080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0293` n `13`; crypto_alt avg `-0.1273` n `239`; crypto_major avg `-0.2534` n `8`; equity avg `-0.1511` n `158`; fx avg `-0.0` n `6`; index avg `-0.0283` n `27`; metal avg `-0.0138` n `20`; unknown avg `51.5001` n `1259`
- 1h: commodity avg `-0.1907` n `13`; crypto_alt avg `-0.7673` n `239`; crypto_major avg `-0.8191` n `8`; equity avg `-0.5297` n `158`; fx avg `-0.0214` n `6`; index avg `-0.0617` n `27`; metal avg `-0.1077` n `20`; unknown avg `32.4958` n `1253`
- 4h: commodity avg `0.0971` n `13`; crypto_alt avg `-0.2684` n `239`; crypto_major avg `-0.4122` n `8`; equity avg `0.3639` n `158`; fx avg `-0.0856` n `6`; index avg `0.0044` n `27`; metal avg `0.0527` n `20`; unknown avg `4.4808` n `1234`
- 24h: commodity avg `0.013` n `13`; crypto_alt avg `-2.2051` n `239`; crypto_major avg `-2.9371` n `8`; equity avg `0.0093` n `158`; fx avg `-0.1047` n `6`; index avg `0.0093` n `27`; metal avg `0.4728` n `20`; unknown avg `1.5893` n `982`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
