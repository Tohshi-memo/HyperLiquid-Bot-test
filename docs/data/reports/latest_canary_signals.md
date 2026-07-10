# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T03:07:27.541965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0348` n `12`; crypto_alt avg `-0.0692` n `229`; crypto_major avg `-0.2009` n `8`; equity avg `0.105` n `91`; fx avg `-0.0026` n `6`; index avg `0.0193` n `25`; metal avg `0.055` n `20`; unknown avg `0.0093` n `765`
- 1h: commodity avg `-0.0152` n `12`; crypto_alt avg `0.0437` n `229`; crypto_major avg `0.0797` n `8`; equity avg `0.2951` n `91`; fx avg `-0.0171` n `6`; index avg `0.0634` n `25`; metal avg `0.1693` n `20`; unknown avg `-0.1145` n `765`
- 4h: commodity avg `0.0667` n `12`; crypto_alt avg `0.669` n `229`; crypto_major avg `0.9203` n `8`; equity avg `0.3427` n `91`; fx avg `-0.0178` n `6`; index avg `0.015` n `25`; metal avg `0.2456` n `20`; unknown avg `0.2657` n `763`
- 24h: commodity avg `-1.0554` n `12`; crypto_alt avg `1.9918` n `229`; crypto_major avg `1.9928` n `8`; equity avg `2.2288` n `91`; fx avg `0.0069` n `6`; index avg `0.5631` n `25`; metal avg `1.0621` n `20`; unknown avg `0.0395` n `746`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
