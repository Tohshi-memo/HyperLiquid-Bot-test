# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T23:07:17.300155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0618` n `12`; crypto_alt avg `0.1947` n `228`; crypto_major avg `0.1815` n `8`; equity avg `0.0167` n `67`; fx avg `0.0005` n `6`; index avg `-0.0687` n `23`; metal avg `0.0002` n `18`; unknown avg `-0.1156` n `386`
- 1h: commodity avg `0.1411` n `12`; crypto_alt avg `-0.2295` n `228`; crypto_major avg `-0.1259` n `8`; equity avg `-0.1423` n `67`; fx avg `0.0048` n `6`; index avg `-0.0292` n `23`; metal avg `-0.027` n `18`; unknown avg `-0.2758` n `386`
- 4h: commodity avg `0.4934` n `12`; crypto_alt avg `-0.4566` n `228`; crypto_major avg `-0.2766` n `8`; equity avg `-0.5722` n `67`; fx avg `0.0023` n `6`; index avg `-0.3158` n `23`; metal avg `-0.1011` n `18`; unknown avg `0.3065` n `386`
- 24h: commodity avg `-0.5436` n `12`; crypto_alt avg `-2.8324` n `228`; crypto_major avg `-2.2331` n `8`; equity avg `-1.4537` n `67`; fx avg `0.1697` n `6`; index avg `0.3095` n `23`; metal avg `-1.1096` n `18`; unknown avg `-1.4948` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
