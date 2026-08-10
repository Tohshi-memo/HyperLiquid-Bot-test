# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T14:22:42.712114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0621` n `12`; crypto_alt avg `-0.0334` n `230`; crypto_major avg `-0.0117` n `8`; equity avg `-0.0806` n `113`; fx avg `-0.0132` n `6`; index avg `-0.0117` n `25`; metal avg `0.0976` n `20`; unknown avg `-0.0041` n `784`
- 1h: commodity avg `0.2015` n `12`; crypto_alt avg `-0.1337` n `230`; crypto_major avg `-0.1181` n `8`; equity avg `0.0024` n `113`; fx avg `0.006` n `6`; index avg `0.044` n `25`; metal avg `0.0238` n `20`; unknown avg `0.0366` n `784`
- 4h: commodity avg `0.4964` n `12`; crypto_alt avg `0.0012` n `230`; crypto_major avg `-0.3123` n `8`; equity avg `-0.6056` n `113`; fx avg `0.0178` n `6`; index avg `-0.0444` n `25`; metal avg `-0.0201` n `20`; unknown avg `0.0129` n `784`
- 24h: commodity avg `0.942` n `12`; crypto_alt avg `0.3652` n `230`; crypto_major avg `-0.6272` n `8`; equity avg `-0.8413` n `113`; fx avg `0.2467` n `6`; index avg `0.0092` n `25`; metal avg `-0.1546` n `20`; unknown avg `59.0005` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
