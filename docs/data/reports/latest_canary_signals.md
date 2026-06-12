# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T21:37:28.314569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0009` n `228`; crypto_major avg `-0.0186` n `8`; equity avg `0.0446` n `74`; fx avg `0.001` n `6`; index avg `-0.0322` n `23`; metal avg `0.0198` n `18`; unknown avg `0.0186` n `643`
- 1h: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.0506` n `228`; crypto_major avg `-0.071` n `8`; equity avg `0.0173` n `74`; fx avg `-0.0113` n `6`; index avg `-0.0484` n `23`; metal avg `-0.0144` n `18`; unknown avg `0.8087` n `643`
- 4h: commodity avg `-0.0215` n `12`; crypto_alt avg `-0.3979` n `228`; crypto_major avg `-0.6964` n `8`; equity avg `-0.3914` n `74`; fx avg `-0.0342` n `6`; index avg `-0.088` n `23`; metal avg `0.1752` n `18`; unknown avg `0.046` n `643`
- 24h: commodity avg `-0.4751` n `12`; crypto_alt avg `-0.3968` n `228`; crypto_major avg `0.4656` n `8`; equity avg `-0.2595` n `74`; fx avg `-0.0285` n `6`; index avg `0.4836` n `23`; metal avg `0.5132` n `18`; unknown avg `41.0977` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
