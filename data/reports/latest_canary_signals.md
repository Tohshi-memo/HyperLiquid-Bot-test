# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T01:37:30.535620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0955` n `12`; crypto_alt avg `0.1502` n `228`; crypto_major avg `0.1095` n `8`; equity avg `0.1086` n `74`; fx avg `0.0028` n `6`; index avg `0.0733` n `23`; metal avg `0.0915` n `18`; unknown avg `0.0451` n `645`
- 1h: commodity avg `-0.1049` n `12`; crypto_alt avg `-0.1031` n `228`; crypto_major avg `-0.2238` n `8`; equity avg `-0.0564` n `74`; fx avg `0.0536` n `6`; index avg `0.0317` n `23`; metal avg `-0.0194` n `18`; unknown avg `0.3576` n `645`
- 4h: commodity avg `-0.3737` n `12`; crypto_alt avg `0.8531` n `228`; crypto_major avg `1.1159` n `8`; equity avg `0.5931` n `74`; fx avg `-0.0265` n `6`; index avg `0.5398` n `23`; metal avg `1.6846` n `18`; unknown avg `1.8853` n `637`
- 24h: commodity avg `-0.9842` n `12`; crypto_alt avg `1.72` n `228`; crypto_major avg `1.94` n `8`; equity avg `1.5988` n `74`; fx avg `0.0377` n `6`; index avg `0.7932` n `23`; metal avg `1.9455` n `18`; unknown avg `1.4495` n `585`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
