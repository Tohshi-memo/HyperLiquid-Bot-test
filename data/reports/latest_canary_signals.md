# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T01:31:10.358398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0507` n `12`; crypto_alt avg `-0.1069` n `233`; crypto_major avg `-0.0718` n `8`; equity avg `0.0012` n `136`; fx avg `0.0` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.013` n `834`
- 1h: commodity avg `-0.0376` n `12`; crypto_alt avg `0.1487` n `233`; crypto_major avg `0.0193` n `8`; equity avg `0.0126` n `136`; fx avg `0.009` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0162` n `20`; unknown avg `0.3207` n `832`
- 4h: commodity avg `-0.0751` n `12`; crypto_alt avg `0.2028` n `233`; crypto_major avg `-0.48` n `8`; equity avg `0.0978` n `136`; fx avg `-0.0018` n `6`; index avg `0.033` n `26`; metal avg `-0.0399` n `20`; unknown avg `4.5657` n `812`
- 24h: commodity avg `-0.5848` n `12`; crypto_alt avg `1.2573` n `233`; crypto_major avg `1.423` n `8`; equity avg `0.809` n `136`; fx avg `-0.1779` n `6`; index avg `0.3201` n `26`; metal avg `0.2075` n `20`; unknown avg `13.9848` n `700`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
