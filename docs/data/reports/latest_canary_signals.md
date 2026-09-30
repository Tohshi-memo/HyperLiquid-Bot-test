# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T18:52:32.829473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0253` n `12`; crypto_alt avg `0.0755` n `234`; crypto_major avg `0.2636` n `8`; equity avg `0.0509` n `142`; fx avg `-0.0056` n `6`; index avg `-0.0065` n `26`; metal avg `-0.012` n `20`; unknown avg `1.8498` n `969`
- 1h: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.7204` n `234`; crypto_major avg `-0.1671` n `8`; equity avg `-0.0619` n `142`; fx avg `-0.0208` n `6`; index avg `-0.0469` n `26`; metal avg `0.0202` n `20`; unknown avg `3.3569` n `967`
- 4h: commodity avg `-0.0414` n `12`; crypto_alt avg `-0.551` n `234`; crypto_major avg `0.4927` n `8`; equity avg `-0.274` n `142`; fx avg `0.0048` n `6`; index avg `-0.1289` n `26`; metal avg `-0.0904` n `20`; unknown avg `4.2796` n `903`
- 24h: commodity avg `0.3378` n `12`; crypto_alt avg `-0.1292` n `234`; crypto_major avg `0.5066` n `8`; equity avg `-0.337` n `142`; fx avg `0.0499` n `6`; index avg `0.002` n `26`; metal avg `-0.215` n `20`; unknown avg `6.6632` n `820`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
