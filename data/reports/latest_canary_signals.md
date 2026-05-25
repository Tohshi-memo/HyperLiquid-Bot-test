# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T16:07:18.140612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1649` n `12`; crypto_alt avg `0.1165` n `228`; crypto_major avg `-0.0166` n `8`; equity avg `-0.0078` n `67`; fx avg `-0.0295` n `6`; index avg `-0.0503` n `23`; metal avg `-0.0273` n `18`; unknown avg `-0.0973` n `405`
- 1h: commodity avg `-0.1656` n `12`; crypto_alt avg `-0.1514` n `228`; crypto_major avg `-0.3035` n `8`; equity avg `-0.0553` n `67`; fx avg `-0.0286` n `6`; index avg `0.0837` n `23`; metal avg `-0.009` n `18`; unknown avg `0.5979` n `405`
- 4h: commodity avg `0.2475` n `12`; crypto_alt avg `0.972` n `228`; crypto_major avg `0.1603` n `8`; equity avg `0.0298` n `67`; fx avg `-0.0476` n `6`; index avg `0.0702` n `23`; metal avg `0.4047` n `18`; unknown avg `0.7954` n `405`
- 24h: commodity avg `-0.4603` n `12`; crypto_alt avg `1.9388` n `228`; crypto_major avg `0.596` n `8`; equity avg `0.9577` n `67`; fx avg `-0.0481` n `6`; index avg `0.5339` n `23`; metal avg `1.4161` n `18`; unknown avg `1.968` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
