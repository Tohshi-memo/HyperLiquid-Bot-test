# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T00:22:20.710382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `-0.0021` n `228`; crypto_major avg `-0.0527` n `8`; equity avg `0.0817` n `73`; fx avg `-0.0623` n `6`; index avg `0.0348` n `23`; metal avg `-0.0473` n `18`; unknown avg `0.8773` n `419`
- 1h: commodity avg `-0.0265` n `12`; crypto_alt avg `0.3224` n `228`; crypto_major avg `0.0608` n `8`; equity avg `0.2291` n `73`; fx avg `-0.0698` n `6`; index avg `0.0617` n `23`; metal avg `0.0608` n `18`; unknown avg `-0.1695` n `419`
- 4h: commodity avg `-0.2787` n `12`; crypto_alt avg `0.1666` n `228`; crypto_major avg `-0.1474` n `8`; equity avg `-1.3275` n `73`; fx avg `-0.101` n `6`; index avg `-0.4109` n `23`; metal avg `0.1752` n `18`; unknown avg `1.0073` n `419`
- 24h: commodity avg `0.3668` n `12`; crypto_alt avg `1.4825` n `228`; crypto_major avg `-1.6766` n `8`; equity avg `-3.5204` n `72`; fx avg `-0.0225` n `6`; index avg `-1.0168` n `23`; metal avg `-1.8849` n `18`; unknown avg `1.7593` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
