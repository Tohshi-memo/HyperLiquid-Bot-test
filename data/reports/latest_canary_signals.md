# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T03:37:30.516738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `13`; crypto_alt avg `0.1005` n `235`; crypto_major avg `0.0253` n `8`; equity avg `-0.0529` n `150`; fx avg `0.0007` n `6`; index avg `-0.0096` n `26`; metal avg `0.009` n `20`; unknown avg `0.0949` n `1077`
- 1h: commodity avg `0.0135` n `13`; crypto_alt avg `-0.4285` n `235`; crypto_major avg `-0.3958` n `8`; equity avg `-0.4181` n `150`; fx avg `0.0075` n `6`; index avg `-0.0745` n `26`; metal avg `-0.0636` n `20`; unknown avg `0.2913` n `1075`
- 4h: commodity avg `0.2305` n `13`; crypto_alt avg `-0.1723` n `235`; crypto_major avg `-0.3279` n `8`; equity avg `-0.5502` n `150`; fx avg `-0.0145` n `6`; index avg `-0.1057` n `26`; metal avg `0.3005` n `20`; unknown avg `0.0613` n `1069`
- 24h: commodity avg `0.4339` n `13`; crypto_alt avg `-0.758` n `235`; crypto_major avg `-1.6477` n `8`; equity avg `-1.3103` n `150`; fx avg `-0.1316` n `6`; index avg `-0.2431` n `26`; metal avg `-0.1773` n `20`; unknown avg `246.9999` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1538`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1336`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1183`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1072`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.098`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0899`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0738`, n `669`, weak_sample_signal
