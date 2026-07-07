# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T20:29:54.014438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0437` n `12`; crypto_alt avg `-0.014` n `229`; crypto_major avg `0.0666` n `8`; equity avg `-0.0256` n `91`; fx avg `0.0124` n `6`; index avg `-0.0144` n `25`; metal avg `-0.0473` n `20`; unknown avg `-0.0303` n `763`
- 1h: commodity avg `-0.0009` n `12`; crypto_alt avg `0.2542` n `229`; crypto_major avg `0.3232` n `8`; equity avg `0.3363` n `91`; fx avg `-0.0021` n `6`; index avg `0.0736` n `25`; metal avg `0.1353` n `20`; unknown avg `0.0601` n `763`
- 4h: commodity avg `0.3583` n `12`; crypto_alt avg `-1.2462` n `229`; crypto_major avg `-0.8817` n `8`; equity avg `-0.5976` n `91`; fx avg `0.004` n `6`; index avg `-0.0652` n `25`; metal avg `-0.3783` n `20`; unknown avg `0.0366` n `761`
- 24h: commodity avg `0.8785` n `12`; crypto_alt avg `-1.7862` n `229`; crypto_major avg `-0.8555` n `8`; equity avg `-3.234` n `91`; fx avg `-0.2422` n `6`; index avg `-0.598` n `25`; metal avg `-0.5139` n `20`; unknown avg `-0.191` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
