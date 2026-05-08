# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T20:07:21.376281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0542` n `12`; crypto_alt avg `-0.0979` n `228`; crypto_major avg `-0.1318` n `8`; equity avg `0.3539` n `65`; fx avg `0.0132` n `5`; index avg `0.0994` n `23`; metal avg `-0.0734` n `18`; unknown avg `-0.0437` n `375`
- 1h: commodity avg `-0.202` n `12`; crypto_alt avg `-0.2003` n `228`; crypto_major avg `-0.1554` n `8`; equity avg `0.4609` n `65`; fx avg `0.0157` n `5`; index avg `0.1142` n `23`; metal avg `-0.0144` n `18`; unknown avg `-0.4027` n `375`
- 4h: commodity avg `-0.577` n `12`; crypto_alt avg `1.1922` n `228`; crypto_major avg `0.9969` n `8`; equity avg `1.0969` n `65`; fx avg `0.0478` n `5`; index avg `0.4023` n `23`; metal avg `0.3454` n `18`; unknown avg `-0.1617` n `375`
- 24h: commodity avg `0.1213` n `12`; crypto_alt avg `2.5697` n `228`; crypto_major avg `1.0996` n `8`; equity avg `3.0326` n `65`; fx avg `0.1968` n `5`; index avg `1.5581` n `23`; metal avg `0.5264` n `18`; unknown avg `0.5447` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
