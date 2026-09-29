# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T08:52:32.265059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.0191` n `234`; crypto_major avg `-0.0865` n `8`; equity avg `-0.0657` n `141`; fx avg `0.003` n `6`; index avg `-0.0121` n `26`; metal avg `0.0202` n `20`; unknown avg `0.0002` n `963`
- 1h: commodity avg `-0.1325` n `12`; crypto_alt avg `-0.0587` n `234`; crypto_major avg `-0.304` n `8`; equity avg `0.1513` n `141`; fx avg `-0.0103` n `6`; index avg `0.0007` n `26`; metal avg `0.0013` n `20`; unknown avg `0.171` n `945`
- 4h: commodity avg `-0.3713` n `12`; crypto_alt avg `1.9055` n `234`; crypto_major avg `1.0169` n `8`; equity avg `0.9307` n `141`; fx avg `-0.0479` n `6`; index avg `0.1333` n `26`; metal avg `0.0655` n `20`; unknown avg `1.3592` n `927`
- 24h: commodity avg `-0.4408` n `12`; crypto_alt avg `1.0558` n `234`; crypto_major avg `0.7268` n `8`; equity avg `-0.0475` n `141`; fx avg `-0.0772` n `6`; index avg `-0.0124` n `26`; metal avg `-0.167` n `20`; unknown avg `54.1084` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
