# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T22:52:23.067162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0874` n `12`; crypto_alt avg `0.0883` n `228`; crypto_major avg `0.225` n `8`; equity avg `0.0194` n `74`; fx avg `-0.0054` n `6`; index avg `0.0071` n `23`; metal avg `0.0159` n `18`; unknown avg `0.2345` n `515`
- 1h: commodity avg `0.0629` n `12`; crypto_alt avg `-0.094` n `228`; crypto_major avg `-0.2475` n `8`; equity avg `-0.1109` n `74`; fx avg `-0.0139` n `6`; index avg `-0.0762` n `23`; metal avg `-0.0015` n `18`; unknown avg `-0.1431` n `515`
- 4h: commodity avg `0.1132` n `12`; crypto_alt avg `0.4651` n `228`; crypto_major avg `0.2091` n `8`; equity avg `0.2012` n `74`; fx avg `-0.076` n `6`; index avg `0.1068` n `23`; metal avg `0.011` n `18`; unknown avg `-0.1856` n `515`
- 24h: commodity avg `0.5595` n `12`; crypto_alt avg `-2.3006` n `228`; crypto_major avg `-2.227` n `8`; equity avg `-0.8571` n `74`; fx avg `0.0198` n `6`; index avg `0.0143` n `23`; metal avg `-0.5391` n `18`; unknown avg `-0.5804` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
