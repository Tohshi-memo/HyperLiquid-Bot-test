# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T05:52:14.648232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `-0.1889` n `228`; crypto_major avg `-0.0444` n `8`; equity avg `-0.1574` n `66`; fx avg `-0.0063` n `6`; index avg `-0.0229` n `23`; metal avg `0.0791` n `18`; unknown avg `-0.0646` n `384`
- 1h: commodity avg `0.0894` n `12`; crypto_alt avg `-0.5855` n `228`; crypto_major avg `-0.2284` n `8`; equity avg `-0.1277` n `66`; fx avg `0.0185` n `6`; index avg `-0.0341` n `23`; metal avg `-0.3379` n `18`; unknown avg `-0.6409` n `384`
- 4h: commodity avg `0.1893` n `12`; crypto_alt avg `-0.4136` n `228`; crypto_major avg `-0.0142` n `8`; equity avg `0.1236` n `66`; fx avg `0.0351` n `6`; index avg `0.1611` n `23`; metal avg `-1.0256` n `18`; unknown avg `-0.4131` n `384`
- 24h: commodity avg `-2.2047` n `12`; crypto_alt avg `2.1984` n `228`; crypto_major avg `3.0325` n `8`; equity avg `2.4164` n `66`; fx avg `0.0499` n `6`; index avg `1.7033` n `23`; metal avg `0.8726` n `18`; unknown avg `5.6858` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
