# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T02:37:15.096550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.0629` n `228`; crypto_major avg `0.047` n `8`; equity avg `-0.0005` n `66`; fx avg `-0.005` n `6`; index avg `0.0098` n `23`; metal avg `-0.3126` n `18`; unknown avg `-0.0959` n `384`
- 1h: commodity avg `-0.0319` n `12`; crypto_alt avg `0.17` n `228`; crypto_major avg `0.1207` n `8`; equity avg `0.1052` n `66`; fx avg `-0.0024` n `6`; index avg `0.0561` n `23`; metal avg `-0.6102` n `18`; unknown avg `0.4131` n `384`
- 4h: commodity avg `-0.4209` n `12`; crypto_alt avg `1.1634` n `228`; crypto_major avg `1.2251` n `8`; equity avg `0.8974` n `66`; fx avg `0.0611` n `6`; index avg `0.4201` n `23`; metal avg `-0.0063` n `18`; unknown avg `4.3924` n `384`
- 24h: commodity avg `-2.4703` n `12`; crypto_alt avg `3.6905` n `228`; crypto_major avg `3.8881` n `8`; equity avg `2.6334` n `66`; fx avg `0.0206` n `6`; index avg `1.7448` n `23`; metal avg `1.7941` n `18`; unknown avg `5.7531` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
