# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T00:37:26.065203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.1659` n `228`; crypto_major avg `-0.1184` n `8`; equity avg `-0.2177` n `86`; fx avg `0.0029` n `6`; index avg `-0.0491` n `23`; metal avg `-0.0047` n `20`; unknown avg `0.0824` n `765`
- 1h: commodity avg `0.0394` n `12`; crypto_alt avg `-0.1223` n `228`; crypto_major avg `-0.5137` n `8`; equity avg `-0.765` n `86`; fx avg `0.0572` n `6`; index avg `-0.1986` n `23`; metal avg `-0.1146` n `20`; unknown avg `0.6468` n `749`
- 4h: commodity avg `0.0027` n `12`; crypto_alt avg `0.6729` n `228`; crypto_major avg `0.7477` n `8`; equity avg `-0.6851` n `86`; fx avg `0.0188` n `6`; index avg `-0.1576` n `23`; metal avg `-0.1367` n `20`; unknown avg `1.536` n `749`
- 24h: commodity avg `0.3351` n `12`; crypto_alt avg `-1.0099` n `228`; crypto_major avg `-1.1795` n `8`; equity avg `-2.6651` n `86`; fx avg `0.06` n `6`; index avg `-0.2512` n `23`; metal avg `0.3145` n `20`; unknown avg `1.6201` n `700`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
