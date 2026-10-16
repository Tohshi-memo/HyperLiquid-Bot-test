# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T17:52:26.630250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1873` n `13`; crypto_alt avg `-0.0243` n `236`; crypto_major avg `-0.1055` n `8`; equity avg `-0.0807` n `151`; fx avg `-0.0014` n `6`; index avg `-0.0205` n `26`; metal avg `-0.0009` n `20`; unknown avg `-0.3493` n `1177`
- 1h: commodity avg `-0.0268` n `13`; crypto_alt avg `-0.1759` n `236`; crypto_major avg `-0.042` n `8`; equity avg `-0.3578` n `151`; fx avg `0.001` n `6`; index avg `-0.0863` n `26`; metal avg `-0.0105` n `20`; unknown avg `0.3944` n `1175`
- 4h: commodity avg `0.5387` n `13`; crypto_alt avg `-1.7798` n `236`; crypto_major avg `-1.2308` n `8`; equity avg `-1.4572` n `151`; fx avg `-0.0173` n `6`; index avg `-0.3127` n `26`; metal avg `-0.2636` n `20`; unknown avg `0.7191` n `998`
- 24h: commodity avg `0.1056` n `13`; crypto_alt avg `-1.7222` n `236`; crypto_major avg `-1.7503` n `8`; equity avg `-2.3632` n `151`; fx avg `-0.0017` n `6`; index avg `-0.4715` n `26`; metal avg `-0.0204` n `20`; unknown avg `-0.2347` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1434`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.094`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0824`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0751`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
