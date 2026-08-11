# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T22:37:26.847205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.0274` n `230`; crypto_major avg `-0.0623` n `8`; equity avg `0.0173` n `113`; fx avg `0.0019` n `6`; index avg `-0.0046` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0481` n `786`
- 1h: commodity avg `0.0469` n `12`; crypto_alt avg `0.067` n `230`; crypto_major avg `0.1393` n `8`; equity avg `0.0356` n `113`; fx avg `0.0104` n `6`; index avg `-0.0315` n `25`; metal avg `0.0399` n `20`; unknown avg `-0.0445` n `786`
- 4h: commodity avg `0.0109` n `12`; crypto_alt avg `0.6315` n `230`; crypto_major avg `1.0767` n `8`; equity avg `0.8681` n `113`; fx avg `0.0054` n `6`; index avg `0.0637` n `25`; metal avg `0.0719` n `20`; unknown avg `0.6345` n `785`
- 24h: commodity avg `0.1499` n `12`; crypto_alt avg `-1.0204` n `230`; crypto_major avg `0.8324` n `8`; equity avg `1.2751` n `113`; fx avg `-0.0577` n `6`; index avg `0.1152` n `25`; metal avg `-0.1882` n `20`; unknown avg `-0.0786` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2222`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2167`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2069`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1989`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
