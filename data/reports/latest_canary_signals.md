# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T18:37:33.752825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `0.0476` n `236`; crypto_major avg `0.0117` n `8`; equity avg `0.0601` n `151`; fx avg `0.0049` n `6`; index avg `0.0216` n `26`; metal avg `0.0011` n `20`; unknown avg `2.5781` n `1193`
- 1h: commodity avg `0.0181` n `13`; crypto_alt avg `0.7355` n `236`; crypto_major avg `0.4123` n `8`; equity avg `0.1568` n `151`; fx avg `-0.0062` n `6`; index avg `0.0258` n `26`; metal avg `0.0171` n `20`; unknown avg `-0.2139` n `1183`
- 4h: commodity avg `0.0671` n `13`; crypto_alt avg `-0.3935` n `236`; crypto_major avg `-0.2943` n `8`; equity avg `-0.1481` n `151`; fx avg `-0.0297` n `6`; index avg `-0.0435` n `26`; metal avg `-0.027` n `20`; unknown avg `2.6641` n `1129`
- 24h: commodity avg `-0.004` n `13`; crypto_alt avg `-0.9647` n `236`; crypto_major avg `-0.2138` n `8`; equity avg `-0.4355` n `151`; fx avg `-0.0165` n `6`; index avg `-0.06` n `26`; metal avg `0.0203` n `20`; unknown avg `4.1492` n `1019`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1715`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1477`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0728`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
