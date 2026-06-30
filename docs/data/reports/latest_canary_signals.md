# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T21:22:33.736142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.45` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `-0.0778` n `228`; crypto_major avg `-0.1206` n `8`; equity avg `-0.0188` n `88`; fx avg `-0.0118` n `6`; index avg `-0.007` n `23`; metal avg `0.0094` n `20`; unknown avg `-0.0805` n `765`
- 1h: commodity avg `0.0234` n `12`; crypto_alt avg `-0.4311` n `228`; crypto_major avg `-0.3166` n `8`; equity avg `0.0165` n `88`; fx avg `-0.0325` n `6`; index avg `-0.0143` n `23`; metal avg `-0.1322` n `20`; unknown avg `-0.1605` n `765`
- 4h: commodity avg `-0.043` n `12`; crypto_alt avg `-0.4654` n `228`; crypto_major avg `0.008` n `8`; equity avg `0.3592` n `88`; fx avg `-0.0162` n `6`; index avg `-0.0563` n `23`; metal avg `-0.1856` n `20`; unknown avg `1.0782` n `763`
- 24h: commodity avg `0.1507` n `12`; crypto_alt avg `-2.5076` n `228`; crypto_major avg `-2.4625` n `8`; equity avg `1.1448` n `88`; fx avg `0.1123` n `6`; index avg `0.2049` n `23`; metal avg `-0.0609` n `20`; unknown avg `7.6076` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
