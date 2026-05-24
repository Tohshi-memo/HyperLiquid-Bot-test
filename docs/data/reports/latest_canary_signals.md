# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T01:52:13.376456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0444` n `12`; crypto_alt avg `-0.0004` n `228`; crypto_major avg `-0.168` n `8`; equity avg `0.0037` n `67`; fx avg `-0.0051` n `6`; index avg `-0.041` n `23`; metal avg `0.0019` n `18`; unknown avg `0.4633` n `396`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `0.1595` n `228`; crypto_major avg `0.2752` n `8`; equity avg `0.1507` n `67`; fx avg `-0.0083` n `6`; index avg `0.0916` n `23`; metal avg `0.1295` n `18`; unknown avg `-0.2735` n `396`
- 4h: commodity avg `0.0951` n `12`; crypto_alt avg `-0.1195` n `228`; crypto_major avg `0.6859` n `8`; equity avg `0.4268` n `67`; fx avg `0.0234` n `6`; index avg `0.2515` n `23`; metal avg `0.4825` n `18`; unknown avg `0.2124` n `396`
- 24h: commodity avg `-2.9465` n `12`; crypto_alt avg `2.4828` n `228`; crypto_major avg `2.6715` n `8`; equity avg `2.1806` n `67`; fx avg `0.0402` n `6`; index avg `1.1073` n `23`; metal avg `1.1518` n `18`; unknown avg `1.6573` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
