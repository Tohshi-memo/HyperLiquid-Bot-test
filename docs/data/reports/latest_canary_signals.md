# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T03:07:14.784762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.0031` n `228`; crypto_major avg `-0.1794` n `8`; equity avg `-0.0166` n `66`; fx avg `0.0244` n `6`; index avg `-0.0056` n `23`; metal avg `0.1474` n `18`; unknown avg `0.7136` n `384`
- 1h: commodity avg `0.125` n `12`; crypto_alt avg `0.1005` n `228`; crypto_major avg `0.1297` n `8`; equity avg `0.0061` n `66`; fx avg `0.0214` n `6`; index avg `0.0022` n `23`; metal avg `-0.6287` n `18`; unknown avg `0.9778` n `384`
- 4h: commodity avg `0.2808` n `12`; crypto_alt avg `1.0303` n `228`; crypto_major avg `1.0873` n `8`; equity avg `0.6733` n `66`; fx avg `0.0974` n `6`; index avg `0.3596` n `23`; metal avg `-0.2259` n `18`; unknown avg `4.0547` n `384`
- 24h: commodity avg `-2.2394` n `12`; crypto_alt avg `3.9507` n `228`; crypto_major avg `3.8558` n `8`; equity avg `2.5585` n `66`; fx avg `0.0728` n `6`; index avg `1.7371` n `23`; metal avg `1.7618` n `18`; unknown avg `5.7872` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
