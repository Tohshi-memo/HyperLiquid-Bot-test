# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T13:07:23.106635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0506` n `12`; crypto_alt avg `0.1952` n `228`; crypto_major avg `0.1249` n `8`; equity avg `0.1446` n `66`; fx avg `-0.0032` n `6`; index avg `0.0576` n `23`; metal avg `0.0648` n `18`; unknown avg `-0.0853` n `386`
- 1h: commodity avg `0.2093` n `12`; crypto_alt avg `0.5421` n `228`; crypto_major avg `0.4087` n `8`; equity avg `0.0494` n `66`; fx avg `-0.0024` n `6`; index avg `-0.0357` n `23`; metal avg `-0.0746` n `18`; unknown avg `-0.123` n `386`
- 4h: commodity avg `1.0765` n `12`; crypto_alt avg `-0.6922` n `228`; crypto_major avg `-0.7393` n `8`; equity avg `-0.4455` n `66`; fx avg `0.0154` n `6`; index avg `-0.4018` n `23`; metal avg `-0.4996` n `18`; unknown avg `0.9202` n `386`
- 24h: commodity avg `-0.6485` n `12`; crypto_alt avg `1.7301` n `228`; crypto_major avg `2.2495` n `8`; equity avg `1.0851` n `66`; fx avg `0.0487` n `6`; index avg `0.8111` n `23`; metal avg `0.0155` n `18`; unknown avg `5.9674` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
