# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T16:07:30.156534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `0.1167` n `239`; crypto_major avg `0.1463` n `8`; equity avg `0.0319` n `158`; fx avg `-0.0096` n `6`; index avg `0.0154` n `27`; metal avg `0.009` n `20`; unknown avg `-0.1843` n `1251`
- 1h: commodity avg `0.0072` n `13`; crypto_alt avg `-0.0918` n `239`; crypto_major avg `-0.1852` n `8`; equity avg `-0.0856` n `158`; fx avg `-0.0167` n `6`; index avg `0.016` n `27`; metal avg `-0.0145` n `20`; unknown avg `0.6828` n `1241`
- 4h: commodity avg `-0.001` n `13`; crypto_alt avg `-0.3377` n `239`; crypto_major avg `-0.3813` n `8`; equity avg `-0.0589` n `158`; fx avg `0.01` n `6`; index avg `0.0415` n `27`; metal avg `-0.012` n `20`; unknown avg `-0.2206` n `1241`
- 24h: commodity avg `0.3239` n `13`; crypto_alt avg `-1.738` n `239`; crypto_major avg `-0.6782` n `8`; equity avg `0.4393` n `158`; fx avg `-0.0061` n `6`; index avg `0.0134` n `27`; metal avg `-0.0087` n `20`; unknown avg `-0.671` n `1107`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
