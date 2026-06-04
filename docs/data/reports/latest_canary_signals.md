# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T21:07:21.607632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.14` n `12`; crypto_alt avg `0.3623` n `228`; crypto_major avg `0.3557` n `8`; equity avg `0.0505` n `74`; fx avg `0.0178` n `6`; index avg `0.0198` n `23`; metal avg `-0.0208` n `18`; unknown avg `0.0011` n `424`
- 1h: commodity avg `0.1643` n `12`; crypto_alt avg `0.4226` n `228`; crypto_major avg `0.7687` n `8`; equity avg `0.0292` n `74`; fx avg `0.0187` n `6`; index avg `-0.0664` n `23`; metal avg `-0.0969` n `18`; unknown avg `0.1261` n `424`
- 4h: commodity avg `0.3432` n `12`; crypto_alt avg `-0.7366` n `228`; crypto_major avg `-0.0905` n `8`; equity avg `-0.6175` n `74`; fx avg `-0.0174` n `6`; index avg `-0.0547` n `23`; metal avg `-0.1786` n `18`; unknown avg `-0.1368` n `424`
- 24h: commodity avg `-0.9444` n `12`; crypto_alt avg `-4.8893` n `228`; crypto_major avg `-3.1668` n `8`; equity avg `-0.72` n `73`; fx avg `0.0435` n `6`; index avg `0.0248` n `23`; metal avg `0.9528` n `18`; unknown avg `-0.221` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
