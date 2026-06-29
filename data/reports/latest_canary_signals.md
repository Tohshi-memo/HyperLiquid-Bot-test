# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T15:52:31.492292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.77` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0526` n `12`; crypto_alt avg `0.0047` n `228`; crypto_major avg `-0.1094` n `8`; equity avg `0.1188` n `88`; fx avg `-0.0172` n `6`; index avg `0.0354` n `23`; metal avg `0.0654` n `20`; unknown avg `0.9219` n `765`
- 1h: commodity avg `0.0459` n `12`; crypto_alt avg `0.5282` n `228`; crypto_major avg `0.5902` n `8`; equity avg `0.6173` n `88`; fx avg `-0.0022` n `6`; index avg `0.1202` n `23`; metal avg `0.0184` n `20`; unknown avg `0.0812` n `764`
- 4h: commodity avg `0.0725` n `12`; crypto_alt avg `0.3049` n `228`; crypto_major avg `0.6205` n `8`; equity avg `-0.269` n `88`; fx avg `0.0443` n `6`; index avg `-0.0487` n `23`; metal avg `-0.0972` n `20`; unknown avg `1.2929` n `764`
- 24h: commodity avg `-0.541` n `12`; crypto_alt avg `-0.013` n `228`; crypto_major avg `0.3269` n `8`; equity avg `0.2851` n `88`; fx avg `0.112` n `6`; index avg `0.031` n `23`; metal avg `-0.4716` n `20`; unknown avg `1.1913` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
