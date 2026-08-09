# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T03:07:22.668827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `0.0486` n `230`; crypto_major avg `-0.003` n `8`; equity avg `0.0485` n `112`; fx avg `0.0065` n `6`; index avg `0.0023` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0305` n `784`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `0.0487` n `230`; crypto_major avg `-0.089` n `8`; equity avg `0.0695` n `112`; fx avg `0.0057` n `6`; index avg `0.0049` n `25`; metal avg `0.0083` n `20`; unknown avg `-0.0968` n `784`
- 4h: commodity avg `0.0293` n `12`; crypto_alt avg `0.1115` n `230`; crypto_major avg `-0.1829` n `8`; equity avg `0.0269` n `112`; fx avg `0.0095` n `6`; index avg `-0.0007` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.1854` n `784`
- 24h: commodity avg `0.2261` n `12`; crypto_alt avg `1.6451` n `230`; crypto_major avg `0.6954` n `8`; equity avg `0.5801` n `112`; fx avg `0.0025` n `6`; index avg `0.0299` n `25`; metal avg `0.0264` n `20`; unknown avg `0.0162` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
