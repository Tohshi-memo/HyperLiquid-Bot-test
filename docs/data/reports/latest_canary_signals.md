# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T01:21:15.188232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0831` n `12`; crypto_alt avg `0.005` n `228`; crypto_major avg `-0.0412` n `8`; equity avg `0.0074` n `67`; fx avg `0.0` n `6`; index avg `0.0041` n `23`; metal avg `-0.0249` n `18`; unknown avg `-0.2983` n `386`
- 1h: commodity avg `0.0076` n `12`; crypto_alt avg `0.3542` n `228`; crypto_major avg `0.2263` n `8`; equity avg `-0.0142` n `67`; fx avg `-0.002` n `6`; index avg `-0.0035` n `23`; metal avg `-0.0638` n `18`; unknown avg `-0.6187` n `386`
- 4h: commodity avg `0.5598` n `12`; crypto_alt avg `-1.2411` n `228`; crypto_major avg `-0.8165` n `8`; equity avg `-0.5991` n `67`; fx avg `-0.0076` n `6`; index avg `-0.2127` n `23`; metal avg `-0.1425` n `18`; unknown avg `-0.928` n `386`
- 24h: commodity avg `-0.1698` n `12`; crypto_alt avg `-3.3361` n `228`; crypto_major avg `-2.3708` n `8`; equity avg `-1.7546` n `67`; fx avg `0.1044` n `6`; index avg `-0.0468` n `23`; metal avg `-0.8589` n `18`; unknown avg `-2.0131` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
