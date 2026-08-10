# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T05:52:31.013412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0874` n `12`; crypto_alt avg `0.0517` n `230`; crypto_major avg `0.0155` n `8`; equity avg `0.0095` n `112`; fx avg `0.011` n `6`; index avg `0.0004` n `25`; metal avg `0.0827` n `20`; unknown avg `-0.2237` n `785`
- 1h: commodity avg `-0.0658` n `12`; crypto_alt avg `0.2417` n `230`; crypto_major avg `0.2466` n `8`; equity avg `0.025` n `112`; fx avg `0.0197` n `6`; index avg `0.0308` n `25`; metal avg `0.1994` n `20`; unknown avg `-0.4089` n `785`
- 4h: commodity avg `-0.1575` n `12`; crypto_alt avg `-0.2294` n `230`; crypto_major avg `-0.2644` n `8`; equity avg `-0.2465` n `112`; fx avg `0.0134` n `6`; index avg `-0.0251` n `25`; metal avg `0.2791` n `20`; unknown avg `-0.4296` n `785`
- 24h: commodity avg `0.1983` n `12`; crypto_alt avg `0.836` n `230`; crypto_major avg `0.1884` n `8`; equity avg `-0.2715` n `112`; fx avg `0.1361` n `6`; index avg `0.0256` n `25`; metal avg `0.0639` n `20`; unknown avg `-0.2912` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1955`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
