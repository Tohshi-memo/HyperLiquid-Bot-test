# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T07:22:30.453715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `13`; crypto_alt avg `-0.0959` n `239`; crypto_major avg `-0.0207` n `8`; equity avg `-0.0117` n `160`; fx avg `0.0034` n `6`; index avg `0.0009` n `27`; metal avg `-0.0495` n `20`; unknown avg `0.0021` n `1261`
- 1h: commodity avg `-0.0985` n `13`; crypto_alt avg `0.1372` n `239`; crypto_major avg `0.1515` n `8`; equity avg `-0.2467` n `160`; fx avg `0.0015` n `6`; index avg `-0.0305` n `27`; metal avg `-0.1304` n `20`; unknown avg `1.2955` n `1251`
- 4h: commodity avg `-0.0418` n `13`; crypto_alt avg `0.6863` n `239`; crypto_major avg `0.476` n `8`; equity avg `0.0099` n `160`; fx avg `-0.075` n `6`; index avg `0.0394` n `27`; metal avg `-0.1279` n `20`; unknown avg `5.7448` n `1215`
- 24h: commodity avg `-0.4123` n `13`; crypto_alt avg `2.6201` n `239`; crypto_major avg `1.1598` n `8`; equity avg `4.8764` n `160`; fx avg `0.0451` n `6`; index avg `0.5465` n `27`; metal avg `0.2216` n `20`; unknown avg `192.7178` n `1063`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
