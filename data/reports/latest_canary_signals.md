# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T10:49:28.469571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.0966` n `230`; crypto_major avg `0.0064` n `8`; equity avg `-0.0102` n `112`; fx avg `0.0099` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0122` n `785`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `-0.0457` n `230`; crypto_major avg `0.1119` n `8`; equity avg `-0.0115` n `112`; fx avg `0.0076` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0134` n `20`; unknown avg `0.0937` n `785`
- 4h: commodity avg `0.0966` n `12`; crypto_alt avg `-0.2797` n `230`; crypto_major avg `-0.0498` n `8`; equity avg `-0.0869` n `112`; fx avg `0.0023` n `6`; index avg `-0.0111` n `25`; metal avg `0.006` n `20`; unknown avg `-0.0486` n `785`
- 24h: commodity avg `0.2687` n `12`; crypto_alt avg `1.1226` n `230`; crypto_major avg `0.344` n `8`; equity avg `0.4256` n `112`; fx avg `0.0057` n `6`; index avg `0.0475` n `25`; metal avg `-0.0004` n `20`; unknown avg `0.2583` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0428`, n `668`, weak_sample_signal
