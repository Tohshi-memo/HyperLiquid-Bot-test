# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T01:52:35.750858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `0.1473` n `230`; crypto_major avg `0.2659` n `8`; equity avg `0.1784` n `113`; fx avg `0.011` n `6`; index avg `0.0323` n `25`; metal avg `0.0484` n `20`; unknown avg `0.4148` n `786`
- 1h: commodity avg `-0.0362` n `12`; crypto_alt avg `0.1904` n `230`; crypto_major avg `0.2089` n `8`; equity avg `0.2921` n `113`; fx avg `0.0254` n `6`; index avg `0.078` n `25`; metal avg `0.0757` n `20`; unknown avg `-0.0033` n `786`
- 4h: commodity avg `0.0991` n `12`; crypto_alt avg `0.3094` n `230`; crypto_major avg `0.3541` n `8`; equity avg `0.5459` n `113`; fx avg `0.0394` n `6`; index avg `0.094` n `25`; metal avg `0.137` n `20`; unknown avg `-0.0051` n `786`
- 24h: commodity avg `0.1586` n `12`; crypto_alt avg `-1.1636` n `230`; crypto_major avg `0.8561` n `8`; equity avg `1.3747` n `113`; fx avg `0.0048` n `6`; index avg `0.0863` n `25`; metal avg `-0.3656` n `20`; unknown avg `-0.0805` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2295`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2236`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2211`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2055`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
