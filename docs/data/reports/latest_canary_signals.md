# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T01:37:26.775161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `0.0435` n `230`; crypto_major avg `0.0609` n `8`; equity avg `0.0707` n `113`; fx avg `0.0014` n `6`; index avg `-0.0019` n `25`; metal avg `0.0518` n `20`; unknown avg `-0.0487` n `786`
- 1h: commodity avg `-0.0246` n `12`; crypto_alt avg `-0.128` n `230`; crypto_major avg `0.0028` n `8`; equity avg `0.1135` n `113`; fx avg `0.0132` n `6`; index avg `0.0206` n `25`; metal avg `-0.1078` n `20`; unknown avg `-0.0839` n `786`
- 4h: commodity avg `-0.153` n `12`; crypto_alt avg `0.3074` n `230`; crypto_major avg `0.1731` n `8`; equity avg `0.2958` n `113`; fx avg `-0.046` n `6`; index avg `0.0266` n `25`; metal avg `0.1084` n `20`; unknown avg `-0.1536` n `786`
- 24h: commodity avg `-0.2181` n `12`; crypto_alt avg `-1.2991` n `230`; crypto_major avg `-0.4231` n `8`; equity avg `2.8512` n `113`; fx avg `-0.0511` n `6`; index avg `0.3628` n `25`; metal avg `0.1885` n `20`; unknown avg `0.0421` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2388`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2033`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
