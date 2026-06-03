# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T22:04:06.727454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.2383` n `12`; crypto_alt avg `0.0953` n `228`; crypto_major avg `-0.0909` n `8`; equity avg `0.2376` n `73`; fx avg `-0.0109` n `6`; index avg `-0.0036` n `23`; metal avg `-0.1025` n `18`; unknown avg `0.8486` n `419`
- 1h: commodity avg `-0.4191` n `12`; crypto_alt avg `1.3908` n `228`; crypto_major avg `0.8995` n `8`; equity avg `-0.159` n `73`; fx avg `-0.0331` n `6`; index avg `-0.1982` n `23`; metal avg `0.0643` n `18`; unknown avg `0.2853` n `419`
- 4h: commodity avg `0.1071` n `12`; crypto_alt avg `0.366` n `228`; crypto_major avg `0.0014` n `8`; equity avg `-1.2587` n `73`; fx avg `-0.0268` n `6`; index avg `-0.4751` n `23`; metal avg `-0.2831` n `18`; unknown avg `0.839` n `419`
- 24h: commodity avg `0.7711` n `12`; crypto_alt avg `2.2388` n `228`; crypto_major avg `-0.6607` n `8`; equity avg `-3.3484` n `72`; fx avg `0.0393` n `6`; index avg `-0.8428` n `23`; metal avg `-2.3009` n `18`; unknown avg `0.5636` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
