# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T21:28:13.419461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `-0.0554` n `230`; crypto_major avg `0.0011` n `8`; equity avg `-0.0371` n `113`; fx avg `0.0016` n `6`; index avg `-0.0113` n `25`; metal avg `-0.0178` n `20`; unknown avg `-0.08` n `785`
- 1h: commodity avg `-0.0484` n `12`; crypto_alt avg `-0.1101` n `230`; crypto_major avg `0.0762` n `8`; equity avg `0.1129` n `113`; fx avg `-0.0018` n `6`; index avg `-0.0087` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0516` n `785`
- 4h: commodity avg `-0.0569` n `12`; crypto_alt avg `0.3113` n `230`; crypto_major avg `0.8336` n `8`; equity avg `0.7247` n `113`; fx avg `0.012` n `6`; index avg `0.0432` n `25`; metal avg `-0.0329` n `20`; unknown avg `0.493` n `785`
- 24h: commodity avg `0.047` n `12`; crypto_alt avg `-1.1902` n `230`; crypto_major avg `0.3894` n `8`; equity avg `1.263` n `113`; fx avg `-0.0672` n `6`; index avg `0.1079` n `25`; metal avg `-0.2496` n `20`; unknown avg `-0.3061` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2174`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2067`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1937`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
