# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T14:43:23.539846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `12`; crypto_alt avg `-0.094` n `230`; crypto_major avg `-0.2399` n `8`; equity avg `-0.1521` n `113`; fx avg `-0.0027` n `6`; index avg `0.0004` n `25`; metal avg `0.0874` n `20`; unknown avg `-0.0188` n `785`
- 1h: commodity avg `0.0568` n `12`; crypto_alt avg `-0.1071` n `230`; crypto_major avg `-0.2222` n `8`; equity avg `0.2079` n `113`; fx avg `0.0014` n `6`; index avg `0.0129` n `25`; metal avg `0.0099` n `20`; unknown avg `-0.0485` n `785`
- 4h: commodity avg `-0.1921` n `12`; crypto_alt avg `-0.2627` n `230`; crypto_major avg `-0.2238` n `8`; equity avg `0.5715` n `113`; fx avg `-0.0135` n `6`; index avg `0.0402` n `25`; metal avg `-0.0793` n `20`; unknown avg `-0.0787` n `785`
- 24h: commodity avg `0.258` n `12`; crypto_alt avg `-1.4362` n `230`; crypto_major avg `-0.5888` n `8`; equity avg `-0.1657` n `113`; fx avg `-0.0612` n `6`; index avg `0.0815` n `25`; metal avg `0.2371` n `20`; unknown avg `-0.1505` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1919`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
