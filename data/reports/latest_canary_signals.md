# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T03:07:32.148884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `-0.145` n `230`; crypto_major avg `-0.2104` n `8`; equity avg `-0.0957` n `113`; fx avg `-0.0024` n `6`; index avg `-0.0195` n `25`; metal avg `0.0013` n `20`; unknown avg `0.0557` n `787`
- 1h: commodity avg `0.0445` n `12`; crypto_alt avg `-0.3257` n `230`; crypto_major avg `-0.2903` n `8`; equity avg `-0.05` n `113`; fx avg `-0.0147` n `6`; index avg `-0.0241` n `25`; metal avg `0.0666` n `20`; unknown avg `-0.1228` n `787`
- 4h: commodity avg `0.0504` n `12`; crypto_alt avg `-0.1172` n `230`; crypto_major avg `-0.1315` n `8`; equity avg `-0.4637` n `113`; fx avg `-0.0593` n `6`; index avg `-0.0698` n `25`; metal avg `-0.1404` n `20`; unknown avg `0.481` n `787`
- 24h: commodity avg `-0.2734` n `12`; crypto_alt avg `0.0239` n `230`; crypto_major avg `0.047` n `8`; equity avg `0.697` n `113`; fx avg `-0.0125` n `6`; index avg `0.1919` n `25`; metal avg `-0.5817` n `20`; unknown avg `1.0635` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2433`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
