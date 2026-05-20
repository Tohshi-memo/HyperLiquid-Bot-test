# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T12:37:18.843081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2853` n `12`; crypto_alt avg `0.3583` n `228`; crypto_major avg `0.2835` n `8`; equity avg `0.038` n `66`; fx avg `-0.0082` n `6`; index avg `0.0315` n `23`; metal avg `0.134` n `18`; unknown avg `0.2697` n `384`
- 1h: commodity avg `-0.5457` n `12`; crypto_alt avg `0.2089` n `228`; crypto_major avg `0.177` n `8`; equity avg `0.1016` n `66`; fx avg `-0.0312` n `6`; index avg `0.0389` n `23`; metal avg `-0.144` n `18`; unknown avg `0.786` n `384`
- 4h: commodity avg `-0.6205` n `12`; crypto_alt avg `0.1414` n `228`; crypto_major avg `0.3758` n `8`; equity avg `0.3041` n `66`; fx avg `0.031` n `6`; index avg `0.1473` n `23`; metal avg `0.2129` n `18`; unknown avg `-0.1261` n `384`
- 24h: commodity avg `-0.7598` n `12`; crypto_alt avg `1.095` n `228`; crypto_major avg `0.9161` n `8`; equity avg `1.6715` n `66`; fx avg `-0.0898` n `6`; index avg `0.2838` n `23`; metal avg `-0.7025` n `18`; unknown avg `0.6516` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
