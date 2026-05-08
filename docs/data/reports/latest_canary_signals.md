# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T21:45:10.073875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0667` n `12`; crypto_alt avg `0.1482` n `228`; crypto_major avg `0.0564` n `8`; equity avg `-0.1049` n `65`; fx avg `-0.0051` n `5`; index avg `0.0528` n `23`; metal avg `-0.0265` n `18`; unknown avg `-0.1332` n `375`
- 1h: commodity avg `0.1211` n `12`; crypto_alt avg `0.5789` n `228`; crypto_major avg `0.2557` n `8`; equity avg `0.0155` n `65`; fx avg `-0.0323` n `5`; index avg `0.078` n `23`; metal avg `-0.0047` n `18`; unknown avg `-0.2758` n `375`
- 4h: commodity avg `-0.3063` n `12`; crypto_alt avg `0.8517` n `228`; crypto_major avg `0.4458` n `8`; equity avg `0.99` n `65`; fx avg `0.0105` n `5`; index avg `0.1238` n `23`; metal avg `-0.0412` n `18`; unknown avg `-0.2454` n `375`
- 24h: commodity avg `-0.7396` n `12`; crypto_alt avg `3.7557` n `228`; crypto_major avg `1.6396` n `8`; equity avg `4.5073` n `65`; fx avg `0.2169` n `5`; index avg `1.7963` n `23`; metal avg `1.2021` n `18`; unknown avg `0.7683` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
