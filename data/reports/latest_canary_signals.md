# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T18:07:17.693600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.128` n `12`; crypto_alt avg `0.15` n `228`; crypto_major avg `0.1127` n `8`; equity avg `0.0042` n `67`; fx avg `0.0029` n `6`; index avg `0.0413` n `23`; metal avg `0.0326` n `18`; unknown avg `0.4542` n `405`
- 1h: commodity avg `0.3909` n `12`; crypto_alt avg `0.0416` n `228`; crypto_major avg `-0.0358` n `8`; equity avg `0.0309` n `67`; fx avg `0.0074` n `6`; index avg `0.1784` n `23`; metal avg `-0.0965` n `18`; unknown avg `0.1074` n `405`
- 4h: commodity avg `-0.4276` n `12`; crypto_alt avg `0.753` n `228`; crypto_major avg `-0.167` n `8`; equity avg `0.0757` n `67`; fx avg `-0.0184` n `6`; index avg `0.1478` n `23`; metal avg `0.3715` n `18`; unknown avg `-0.192` n `405`
- 24h: commodity avg `-1.0394` n `12`; crypto_alt avg `2.3489` n `228`; crypto_major avg `0.7166` n `8`; equity avg `0.8964` n `67`; fx avg `-0.0229` n `6`; index avg `0.5709` n `23`; metal avg `1.55` n `18`; unknown avg `1.2152` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
