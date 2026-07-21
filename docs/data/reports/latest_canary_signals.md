# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T10:22:29.032537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0275` n `12`; crypto_alt avg `-0.0021` n `230`; crypto_major avg `-0.0415` n `8`; equity avg `0.0527` n `98`; fx avg `0.0003` n `6`; index avg `0.0183` n `25`; metal avg `0.07` n `20`; unknown avg `0.0084` n `771`
- 1h: commodity avg `0.1441` n `12`; crypto_alt avg `0.1658` n `230`; crypto_major avg `0.1284` n `8`; equity avg `-0.0932` n `98`; fx avg `0.0025` n `6`; index avg `-0.0024` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.0051` n `771`
- 4h: commodity avg `0.2049` n `12`; crypto_alt avg `0.0382` n `230`; crypto_major avg `0.3539` n `8`; equity avg `0.5217` n `98`; fx avg `0.0298` n `6`; index avg `0.0774` n `25`; metal avg `0.1329` n `20`; unknown avg `0.0403` n `771`
- 24h: commodity avg `0.4025` n `12`; crypto_alt avg `2.2572` n `230`; crypto_major avg `2.6466` n `8`; equity avg `1.657` n `98`; fx avg `-0.0885` n `6`; index avg `0.2702` n `25`; metal avg `0.6287` n `20`; unknown avg `0.165` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0849`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0698`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
