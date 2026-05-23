# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T03:07:16.788107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `0.101` n `228`; crypto_major avg `0.0601` n `8`; equity avg `0.0695` n `67`; fx avg `0.0014` n `6`; index avg `0.0518` n `23`; metal avg `0.028` n `18`; unknown avg `0.1695` n `386`
- 1h: commodity avg `-0.194` n `12`; crypto_alt avg `0.1886` n `228`; crypto_major avg `0.2255` n `8`; equity avg `0.114` n `67`; fx avg `0.0014` n `6`; index avg `0.0369` n `23`; metal avg `0.0376` n `18`; unknown avg `-0.2723` n `386`
- 4h: commodity avg `0.2374` n `12`; crypto_alt avg `-0.3944` n `228`; crypto_major avg `-0.5213` n `8`; equity avg `-0.2869` n `67`; fx avg `-0.0058` n `6`; index avg `-0.0525` n `23`; metal avg `-0.0783` n `18`; unknown avg `-1.1492` n `386`
- 24h: commodity avg `0.0036` n `12`; crypto_alt avg `-3.518` n `228`; crypto_major avg `-2.6267` n `8`; equity avg `-1.63` n `67`; fx avg `0.0777` n `6`; index avg `0.0714` n `23`; metal avg `-0.6904` n `18`; unknown avg `-2.1516` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
