# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T03:52:31.684818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `13`; crypto_alt avg `0.6015` n `236`; crypto_major avg `0.3963` n `8`; equity avg `0.4984` n `151`; fx avg `0.0281` n `6`; index avg `0.0901` n `26`; metal avg `0.0971` n `20`; unknown avg `4.0816` n `1136`
- 1h: commodity avg `-0.0228` n `13`; crypto_alt avg `0.0135` n `236`; crypto_major avg `0.013` n `8`; equity avg `0.3582` n `151`; fx avg `0.0338` n `6`; index avg `0.0593` n `26`; metal avg `0.0664` n `20`; unknown avg `3.1969` n `1134`
- 4h: commodity avg `-0.1171` n `13`; crypto_alt avg `-0.1327` n `236`; crypto_major avg `-0.1235` n `8`; equity avg `0.8093` n `151`; fx avg `0.0855` n `6`; index avg `0.1216` n `26`; metal avg `0.2509` n `20`; unknown avg `1.0048` n `1128`
- 24h: commodity avg `-0.0681` n `13`; crypto_alt avg `3.7039` n `236`; crypto_major avg `2.1859` n `8`; equity avg `2.6424` n `151`; fx avg `0.0419` n `6`; index avg `0.4633` n `26`; metal avg `0.5352` n `20`; unknown avg `26.7409` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.097`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0902`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0879`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0744`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0699`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0666`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
