# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T16:22:30.399768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0593` n `12`; crypto_alt avg `0.173` n `230`; crypto_major avg `0.3165` n `8`; equity avg `0.281` n `108`; fx avg `0.0077` n `6`; index avg `0.0386` n `25`; metal avg `0.042` n `20`; unknown avg `-0.0564` n `782`
- 1h: commodity avg `0.1463` n `12`; crypto_alt avg `0.1677` n `230`; crypto_major avg `0.3687` n `8`; equity avg `0.0649` n `108`; fx avg `0.0132` n `6`; index avg `-0.0405` n `25`; metal avg `-0.1244` n `20`; unknown avg `-0.0145` n `782`
- 4h: commodity avg `-0.0855` n `12`; crypto_alt avg `-0.0919` n `230`; crypto_major avg `0.2865` n `8`; equity avg `0.0727` n `108`; fx avg `-0.0027` n `6`; index avg `-0.0637` n `25`; metal avg `-0.0765` n `20`; unknown avg `-0.1135` n `782`
- 24h: commodity avg `0.0484` n `12`; crypto_alt avg `0.8446` n `230`; crypto_major avg `0.9141` n `8`; equity avg `0.1848` n `108`; fx avg `0.0309` n `6`; index avg `0.0935` n `25`; metal avg `0.6486` n `20`; unknown avg `0.7944` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
