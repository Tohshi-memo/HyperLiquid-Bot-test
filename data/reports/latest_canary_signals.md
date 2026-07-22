# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T11:52:26.151879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1074` n `12`; crypto_alt avg `-0.0098` n `230`; crypto_major avg `-0.0298` n `8`; equity avg `-0.1157` n `98`; fx avg `-0.0023` n `6`; index avg `-0.0217` n `25`; metal avg `0.0` n `20`; unknown avg `-0.0713` n `773`
- 1h: commodity avg `0.1016` n `12`; crypto_alt avg `-0.1133` n `230`; crypto_major avg `-0.1915` n `8`; equity avg `-0.3914` n `98`; fx avg `0.0006` n `6`; index avg `-0.0846` n `25`; metal avg `0.0011` n `20`; unknown avg `0.3603` n `773`
- 4h: commodity avg `0.0011` n `12`; crypto_alt avg `0.5647` n `230`; crypto_major avg `0.5083` n `8`; equity avg `-0.0687` n `98`; fx avg `-0.0028` n `6`; index avg `0.0021` n `25`; metal avg `0.1001` n `20`; unknown avg `0.4827` n `773`
- 24h: commodity avg `0.6367` n `12`; crypto_alt avg `-0.5586` n `230`; crypto_major avg `-1.3402` n `8`; equity avg `0.309` n `98`; fx avg `-0.014` n `6`; index avg `-0.0568` n `25`; metal avg `0.3763` n `20`; unknown avg `0.4405` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1044`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0851`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0752`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0705`, n `666`, weak_sample_signal
