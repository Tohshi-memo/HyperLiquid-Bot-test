# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T01:07:17.692007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0325` n `12`; crypto_alt avg `0.3019` n `228`; crypto_major avg `0.1634` n `8`; equity avg `0.0562` n `67`; fx avg `-0.0014` n `6`; index avg `0.0539` n `23`; metal avg `-0.0025` n `18`; unknown avg `-0.0976` n `386`
- 1h: commodity avg `0.22` n `12`; crypto_alt avg `0.2594` n `228`; crypto_major avg `0.0184` n `8`; equity avg `-0.1646` n `67`; fx avg `-0.002` n `6`; index avg `-0.096` n `23`; metal avg `-0.0519` n `18`; unknown avg `-0.4821` n `386`
- 4h: commodity avg `0.6433` n `12`; crypto_alt avg `-1.1023` n `228`; crypto_major avg `-0.5836` n `8`; equity avg `-0.6097` n `67`; fx avg `-0.0043` n `6`; index avg `-0.226` n `23`; metal avg `-0.1231` n `18`; unknown avg `-0.9679` n `386`
- 24h: commodity avg `-0.043` n `12`; crypto_alt avg `-3.1756` n `228`; crypto_major avg `-2.4059` n `8`; equity avg `-1.6783` n `67`; fx avg `0.125` n `6`; index avg `-0.0131` n `23`; metal avg `-0.7801` n `18`; unknown avg `-1.8409` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
