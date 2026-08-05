# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T12:37:25.538812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0681` n `12`; crypto_alt avg `-0.05` n `230`; crypto_major avg `0.0223` n `8`; equity avg `0.2053` n `108`; fx avg `0.0035` n `6`; index avg `0.0176` n `25`; metal avg `-0.1448` n `20`; unknown avg `0.0018` n `782`
- 1h: commodity avg `0.0686` n `12`; crypto_alt avg `0.2609` n `230`; crypto_major avg `0.4184` n `8`; equity avg `0.1259` n `108`; fx avg `-0.0101` n `6`; index avg `0.0035` n `25`; metal avg `-0.0461` n `20`; unknown avg `0.0246` n `782`
- 4h: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.0127` n `230`; crypto_major avg `0.0864` n `8`; equity avg `0.3458` n `108`; fx avg `-0.0252` n `6`; index avg `0.0822` n `25`; metal avg `0.0746` n `20`; unknown avg `0.6042` n `781`
- 24h: commodity avg `-0.3576` n `12`; crypto_alt avg `0.7231` n `230`; crypto_major avg `0.5403` n `8`; equity avg `2.0602` n `108`; fx avg `0.0376` n `6`; index avg `0.5695` n `25`; metal avg `0.637` n `20`; unknown avg `0.0456` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
