# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T04:07:20.637865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0928` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0338` n `12`; crypto_alt avg `0.5793` n `228`; crypto_major avg `0.5069` n `8`; equity avg `0.1486` n `74`; fx avg `-0.0009` n `6`; index avg `0.043` n `23`; metal avg `0.0755` n `18`; unknown avg `0.2584` n `424`
- 1h: commodity avg `-0.1228` n `12`; crypto_alt avg `0.7374` n `228`; crypto_major avg `0.5462` n `8`; equity avg `-0.0735` n `74`; fx avg `0.0047` n `6`; index avg `-0.0765` n `23`; metal avg `0.1556` n `18`; unknown avg `1.4268` n `424`
- 4h: commodity avg `-0.0259` n `12`; crypto_alt avg `-2.0978` n `228`; crypto_major avg `-1.4235` n `8`; equity avg `-0.3866` n `74`; fx avg `0.1382` n `6`; index avg `-0.3307` n `23`; metal avg `-0.6351` n `18`; unknown avg `0.408` n `424`
- 24h: commodity avg `-0.2009` n `12`; crypto_alt avg `-6.3158` n `228`; crypto_major avg `-5.1283` n `8`; equity avg `-1.6689` n `73`; fx avg `0.1997` n `6`; index avg `-0.5607` n `23`; metal avg `-0.5149` n `18`; unknown avg `-1.6221` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
