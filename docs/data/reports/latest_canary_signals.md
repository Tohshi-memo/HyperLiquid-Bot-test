# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T02:22:28.638070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `0.1263` n `233`; crypto_major avg `0.0087` n `8`; equity avg `-0.0074` n `136`; fx avg `0.0043` n `6`; index avg `0.0001` n `26`; metal avg `-0.0006` n `20`; unknown avg `-0.0494` n `838`
- 1h: commodity avg `-0.0518` n `12`; crypto_alt avg `0.1727` n `233`; crypto_major avg `0.0241` n `8`; equity avg `-0.0106` n `136`; fx avg `0.0054` n `6`; index avg `-0.0131` n `26`; metal avg `-0.0136` n `20`; unknown avg `2.3006` n `832`
- 4h: commodity avg `-0.0727` n `12`; crypto_alt avg `0.9566` n `233`; crypto_major avg `-0.0189` n `8`; equity avg `0.0945` n `136`; fx avg `0.0075` n `6`; index avg `0.0138` n `26`; metal avg `-0.04` n `20`; unknown avg `-0.2123` n `820`
- 24h: commodity avg `-0.6459` n `12`; crypto_alt avg `1.6894` n `233`; crypto_major avg `1.4139` n `8`; equity avg `0.8881` n `136`; fx avg `-0.157` n `6`; index avg `0.2923` n `26`; metal avg `0.2274` n `20`; unknown avg `29.7759` n `700`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
