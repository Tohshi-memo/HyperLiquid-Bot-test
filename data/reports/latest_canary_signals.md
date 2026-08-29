# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T07:07:24.520238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0491` n `12`; crypto_alt avg `0.0201` n `231`; crypto_major avg `0.0746` n `8`; equity avg `0.0153` n `127`; fx avg `0.0122` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0086` n `20`; unknown avg `0.0511` n `793`
- 1h: commodity avg `0.0363` n `12`; crypto_alt avg `-0.1037` n `231`; crypto_major avg `-0.0595` n `8`; equity avg `0.0311` n `127`; fx avg `-0.0053` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0077` n `20`; unknown avg `0.1042` n `793`
- 4h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.2397` n `231`; crypto_major avg `-0.0838` n `8`; equity avg `0.0976` n `127`; fx avg `0.0017` n `6`; index avg `0.0112` n `26`; metal avg `0.007` n `20`; unknown avg `-0.0087` n `761`
- 24h: commodity avg `-0.1083` n `12`; crypto_alt avg `-1.9705` n `231`; crypto_major avg `-2.4706` n `8`; equity avg `-1.4559` n `127`; fx avg `-0.0346` n `6`; index avg `-0.1432` n `26`; metal avg `-0.5701` n `20`; unknown avg `-0.2852` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
