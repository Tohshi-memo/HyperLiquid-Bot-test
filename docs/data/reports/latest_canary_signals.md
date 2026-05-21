# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T02:22:15.557463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0317` n `12`; crypto_alt avg `0.2311` n `228`; crypto_major avg `0.1868` n `8`; equity avg `0.0758` n `66`; fx avg `-0.007` n `6`; index avg `0.0218` n `23`; metal avg `-0.1491` n `18`; unknown avg `0.5035` n `384`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `0.2117` n `228`; crypto_major avg `-0.0955` n `8`; equity avg `0.0905` n `66`; fx avg `0.0059` n `6`; index avg `0.0911` n `23`; metal avg `-0.3038` n `18`; unknown avg `0.943` n `384`
- 4h: commodity avg `-0.1173` n `12`; crypto_alt avg `1.3759` n `228`; crypto_major avg `1.5011` n `8`; equity avg `1.0382` n `66`; fx avg `0.0686` n `6`; index avg `0.4643` n `23`; metal avg `0.4603` n `18`; unknown avg `4.4823` n `384`
- 24h: commodity avg `-2.2314` n `12`; crypto_alt avg `3.6442` n `228`; crypto_major avg `3.627` n `8`; equity avg `2.1123` n `66`; fx avg `0.071` n `6`; index avg `1.4063` n `23`; metal avg `1.6059` n `18`; unknown avg `5.6569` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
