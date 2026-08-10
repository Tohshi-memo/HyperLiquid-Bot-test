# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T13:22:33.884222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0328` n `12`; crypto_alt avg `-0.0229` n `230`; crypto_major avg `-0.0225` n `8`; equity avg `0.0458` n `113`; fx avg `0.0065` n `6`; index avg `0.0067` n `25`; metal avg `0.0183` n `20`; unknown avg `0.1193` n `784`
- 1h: commodity avg `0.0802` n `12`; crypto_alt avg `-0.0944` n `230`; crypto_major avg `-0.424` n `8`; equity avg `-0.0817` n `113`; fx avg `0.0283` n `6`; index avg `-0.0079` n `25`; metal avg `0.0066` n `20`; unknown avg `0.1074` n `784`
- 4h: commodity avg `0.229` n `12`; crypto_alt avg `0.0628` n `230`; crypto_major avg `-0.3307` n `8`; equity avg `-0.7009` n `113`; fx avg `0.0022` n `6`; index avg `-0.095` n `25`; metal avg `-0.0746` n `20`; unknown avg `-0.023` n `784`
- 24h: commodity avg `0.7242` n `12`; crypto_alt avg `0.5902` n `230`; crypto_major avg `-0.3791` n `8`; equity avg `-0.8181` n `113`; fx avg `0.249` n `6`; index avg `-0.0256` n `25`; metal avg `-0.1847` n `20`; unknown avg `108.5671` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
