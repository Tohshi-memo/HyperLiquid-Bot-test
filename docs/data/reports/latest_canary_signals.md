# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T23:22:29.223820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.0321` n `231`; crypto_major avg `-0.0241` n `8`; equity avg `-0.0026` n `128`; fx avg `0.0` n `6`; index avg `0.0065` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.0027` n `793`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `0.1569` n `231`; crypto_major avg `0.1781` n `8`; equity avg `0.0128` n `128`; fx avg `0.0012` n `6`; index avg `0.0128` n `26`; metal avg `0.0043` n `20`; unknown avg `-0.0246` n `789`
- 4h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.1131` n `231`; crypto_major avg `-0.0208` n `8`; equity avg `0.1431` n `128`; fx avg `-0.0011` n `6`; index avg `0.0264` n `26`; metal avg `0.0064` n `20`; unknown avg `0.3458` n `774`
- 24h: commodity avg `-0.001` n `12`; crypto_alt avg `0.3404` n `231`; crypto_major avg `0.9205` n `8`; equity avg `0.4339` n `128`; fx avg `-0.0234` n `6`; index avg `0.0912` n `26`; metal avg `0.1305` n `20`; unknown avg `0.0403` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
