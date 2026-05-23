# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T02:37:18.204941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.21` n `12`; crypto_alt avg `-0.0567` n `228`; crypto_major avg `0.0531` n `8`; equity avg `0.0128` n `67`; fx avg `0.0` n `6`; index avg `-0.0087` n `23`; metal avg `0.0006` n `18`; unknown avg `-0.0779` n `386`
- 1h: commodity avg `-0.2087` n `12`; crypto_alt avg `-0.003` n `228`; crypto_major avg `-0.1507` n `8`; equity avg `0.0284` n `67`; fx avg `-0.0023` n `6`; index avg `0.012` n `23`; metal avg `0.0139` n `18`; unknown avg `-0.1963` n `386`
- 4h: commodity avg `0.3456` n `12`; crypto_alt avg `-0.4284` n `228`; crypto_major avg `-0.5495` n `8`; equity avg `-0.3983` n `67`; fx avg `-0.0054` n `6`; index avg `-0.1391` n `23`; metal avg `-0.1477` n `18`; unknown avg `-1.0607` n `386`
- 24h: commodity avg `-0.1085` n `12`; crypto_alt avg `-3.5503` n `228`; crypto_major avg `-2.8411` n `8`; equity avg `-1.6528` n `67`; fx avg `0.1106` n `6`; index avg `0.0404` n `23`; metal avg `-0.6481` n `18`; unknown avg `-2.1618` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
