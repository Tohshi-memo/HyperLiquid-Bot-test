# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T23:37:15.163355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1092` n `12`; crypto_alt avg `-0.1646` n `228`; crypto_major avg `-0.0094` n `8`; equity avg `-0.0374` n `67`; fx avg `0.0` n `6`; index avg `-0.0241` n `23`; metal avg `-0.016` n `18`; unknown avg `-0.0607` n `386`
- 1h: commodity avg `0.3697` n `12`; crypto_alt avg `-0.2733` n `228`; crypto_major avg `-0.1325` n `8`; equity avg `-0.1222` n `67`; fx avg `0.0027` n `6`; index avg `-0.076` n `23`; metal avg `-0.0413` n `18`; unknown avg `0.2522` n `386`
- 4h: commodity avg `0.7287` n `12`; crypto_alt avg `-0.2276` n `228`; crypto_major avg `-0.2228` n `8`; equity avg `-0.4547` n `67`; fx avg `0.0015` n `6`; index avg `-0.2525` n `23`; metal avg `-0.0731` n `18`; unknown avg `-0.5665` n `386`
- 24h: commodity avg `-0.0708` n `12`; crypto_alt avg `-3.2704` n `228`; crypto_major avg `-2.5959` n `8`; equity avg `-1.5291` n `67`; fx avg `0.191` n `6`; index avg `0.2172` n `23`; metal avg `-0.9931` n `18`; unknown avg `-1.6454` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
