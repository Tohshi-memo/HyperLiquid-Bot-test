# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T15:07:29.445712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0457` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0539` n `12`; crypto_alt avg `0.0504` n `230`; crypto_major avg `0.1144` n `8`; equity avg `0.0854` n `102`; fx avg `-0.013` n `6`; index avg `0.0534` n `25`; metal avg `0.0662` n `20`; unknown avg `0.1177` n `774`
- 1h: commodity avg `-0.1216` n `12`; crypto_alt avg `-1.3634` n `230`; crypto_major avg `-1.1793` n `8`; equity avg `-0.8638` n `102`; fx avg `-0.0379` n `6`; index avg `-0.1336` n `25`; metal avg `0.0379` n `20`; unknown avg `-0.0764` n `774`
- 4h: commodity avg `0.0356` n `12`; crypto_alt avg `-1.6147` n `230`; crypto_major avg `-1.4611` n `8`; equity avg `-2.6016` n `102`; fx avg `-0.051` n `6`; index avg `-0.484` n `25`; metal avg `-0.1207` n `20`; unknown avg `-0.0005` n `774`
- 24h: commodity avg `-0.5147` n `12`; crypto_alt avg `-0.963` n `230`; crypto_major avg `-0.3693` n `8`; equity avg `-1.5852` n `102`; fx avg `0.0385` n `6`; index avg `-0.3587` n `25`; metal avg `0.2297` n `20`; unknown avg `-0.2271` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
