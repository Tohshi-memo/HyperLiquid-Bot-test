# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T20:22:23.737145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `0.4324` n `228`; crypto_major avg `0.5473` n `8`; equity avg `-0.0154` n `74`; fx avg `-0.0042` n `6`; index avg `-0.0594` n `23`; metal avg `-0.0456` n `18`; unknown avg `-0.0206` n `424`
- 1h: commodity avg `-0.1305` n `12`; crypto_alt avg `-0.6489` n `228`; crypto_major avg `-0.3237` n `8`; equity avg `-0.6034` n `74`; fx avg `-0.0086` n `6`; index avg `-0.2119` n `23`; metal avg `-0.1004` n `18`; unknown avg `-0.1649` n `424`
- 4h: commodity avg `0.071` n `12`; crypto_alt avg `-0.6125` n `228`; crypto_major avg `-0.3139` n `8`; equity avg `-0.6565` n `74`; fx avg `-0.0475` n `6`; index avg `0.0245` n `23`; metal avg `-0.0942` n `18`; unknown avg `0.8999` n `424`
- 24h: commodity avg `-0.7874` n `12`; crypto_alt avg `-5.0187` n `228`; crypto_major avg `-3.4264` n `8`; equity avg `-1.3147` n `73`; fx avg `0.0099` n `6`; index avg `-0.0942` n `23`; metal avg `0.8908` n `18`; unknown avg `-0.0556` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
