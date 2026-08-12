# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T09:22:32.844390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0375` n `12`; crypto_alt avg `0.1657` n `230`; crypto_major avg `0.1165` n `8`; equity avg `0.0045` n `113`; fx avg `-0.0138` n `6`; index avg `0.0108` n `25`; metal avg `0.1345` n `20`; unknown avg `-0.0006` n `786`
- 1h: commodity avg `-0.0561` n `12`; crypto_alt avg `-0.0239` n `230`; crypto_major avg `0.0528` n `8`; equity avg `0.0593` n `113`; fx avg `-0.0114` n `6`; index avg `0.0337` n `25`; metal avg `0.131` n `20`; unknown avg `-0.1236` n `786`
- 4h: commodity avg `-0.0696` n `12`; crypto_alt avg `-0.5616` n `230`; crypto_major avg `-0.0126` n `8`; equity avg `0.684` n `113`; fx avg `0.0126` n `6`; index avg `0.1392` n `25`; metal avg `0.2944` n `20`; unknown avg `-0.1804` n `770`
- 24h: commodity avg `-0.1721` n `12`; crypto_alt avg `-1.305` n `230`; crypto_major avg `0.5883` n `8`; equity avg `2.6702` n `113`; fx avg `-0.0035` n `6`; index avg `0.2803` n `25`; metal avg `0.2893` n `20`; unknown avg `-0.2871` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2432`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2255`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
