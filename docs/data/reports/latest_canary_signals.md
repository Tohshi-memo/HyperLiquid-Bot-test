# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T22:52:29.615963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0177` n `12`; crypto_alt avg `0.2218` n `234`; crypto_major avg `0.2009` n `8`; equity avg `0.0205` n `137`; fx avg `-0.0029` n `6`; index avg `0.0076` n `27`; metal avg `-0.0146` n `20`; unknown avg `0.1123` n `919`
- 1h: commodity avg `-0.0037` n `12`; crypto_alt avg `0.2376` n `234`; crypto_major avg `0.3559` n `8`; equity avg `0.0733` n `137`; fx avg `0.0135` n `6`; index avg `0.0149` n `27`; metal avg `0.0274` n `20`; unknown avg `0.9711` n `885`
- 4h: commodity avg `-0.0015` n `12`; crypto_alt avg `-0.0077` n `234`; crypto_major avg `0.0969` n `8`; equity avg `0.1914` n `137`; fx avg `0.001` n `6`; index avg `0.0503` n `27`; metal avg `-0.0452` n `20`; unknown avg `1.1734` n `845`
- 24h: commodity avg `0.4738` n `12`; crypto_alt avg `-3.9849` n `234`; crypto_major avg `-4.2635` n `8`; equity avg `-1.2348` n `137`; fx avg `0.2367` n `6`; index avg `-0.053` n `27`; metal avg `0.188` n `20`; unknown avg `2.1277` n `802`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
