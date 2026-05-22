# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T14:52:21.554593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `-0.3546` n `228`; crypto_major avg `-0.2567` n `8`; equity avg `-0.0306` n `67`; fx avg `0.0142` n `6`; index avg `-0.0193` n `23`; metal avg `0.1057` n `18`; unknown avg `-0.0797` n `386`
- 1h: commodity avg `-0.2641` n `12`; crypto_alt avg `-1.0139` n `228`; crypto_major avg `-0.8975` n `8`; equity avg `-0.3864` n `67`; fx avg `-0.0024` n `6`; index avg `-0.1606` n `23`; metal avg `-0.3708` n `18`; unknown avg `-0.2393` n `386`
- 4h: commodity avg `-0.626` n `12`; crypto_alt avg `-0.5537` n `228`; crypto_major avg `-0.1954` n `8`; equity avg `0.1257` n `67`; fx avg `-0.0138` n `6`; index avg `0.3915` n `23`; metal avg `-0.7181` n `18`; unknown avg `0.5258` n `386`
- 24h: commodity avg `-1.8252` n `12`; crypto_alt avg `1.4273` n `228`; crypto_major avg `0.0036` n `8`; equity avg `0.9798` n `67`; fx avg `0.1305` n `6`; index avg `1.1636` n `23`; metal avg `-0.0556` n `18`; unknown avg `0.8335` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0429`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0419`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0385`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0384`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0367`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.031`, n `668`, weak_sample_signal
