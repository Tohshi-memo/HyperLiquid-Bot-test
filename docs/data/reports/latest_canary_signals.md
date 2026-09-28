# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T11:07:28.173729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `-0.1347` n `234`; crypto_major avg `-0.0401` n `8`; equity avg `-0.0124` n `141`; fx avg `-0.0025` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0669` n `20`; unknown avg `1.6252` n `960`
- 1h: commodity avg `-0.0613` n `12`; crypto_alt avg `0.4247` n `234`; crypto_major avg `0.3479` n `8`; equity avg `0.1199` n `141`; fx avg `0.0055` n `6`; index avg `0.0097` n `26`; metal avg `-0.0302` n `20`; unknown avg `2.6493` n `960`
- 4h: commodity avg `0.3494` n `12`; crypto_alt avg `-0.6348` n `234`; crypto_major avg `0.2144` n `8`; equity avg `-0.4149` n `141`; fx avg `-0.0587` n `6`; index avg `-0.0372` n `26`; metal avg `0.0078` n `20`; unknown avg `23.4365` n `942`
- 24h: commodity avg `-0.0346` n `12`; crypto_alt avg `-3.744` n `234`; crypto_major avg `-2.6993` n `8`; equity avg `-2.7175` n `141`; fx avg `0.0229` n `6`; index avg `-0.2704` n `26`; metal avg `-0.9236` n `20`; unknown avg `8.3662` n `814`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
