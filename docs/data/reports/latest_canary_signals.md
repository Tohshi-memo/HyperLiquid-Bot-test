# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T22:58:47.759713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `12`; crypto_alt avg `0.2643` n `234`; crypto_major avg `0.1468` n `8`; equity avg `0.007` n `137`; fx avg `-0.0029` n `6`; index avg `0.0075` n `27`; metal avg `-0.0286` n `20`; unknown avg `0.1107` n `919`
- 1h: commodity avg `-0.0016` n `12`; crypto_alt avg `0.2802` n `234`; crypto_major avg `0.3016` n `8`; equity avg `0.0597` n `137`; fx avg `0.0135` n `6`; index avg `0.0148` n `27`; metal avg `0.0134` n `20`; unknown avg `0.9707` n `885`
- 4h: commodity avg `0.0006` n `12`; crypto_alt avg `0.0354` n `234`; crypto_major avg `0.0425` n `8`; equity avg `0.1777` n `137`; fx avg `0.001` n `6`; index avg `0.0502` n `27`; metal avg `-0.0592` n `20`; unknown avg `1.1875` n `845`
- 24h: commodity avg `0.4759` n `12`; crypto_alt avg `-3.9438` n `234`; crypto_major avg `-4.3157` n `8`; equity avg `-1.2482` n `137`; fx avg `0.2367` n `6`; index avg `-0.0531` n `27`; metal avg `0.1739` n `20`; unknown avg `2.0497` n `802`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
