# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T01:22:30.291657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0308` n `13`; crypto_alt avg `-0.265` n `235`; crypto_major avg `-0.2013` n `8`; equity avg `-0.1625` n `144`; fx avg `0.0293` n `6`; index avg `-0.0396` n `26`; metal avg `-0.0932` n `20`; unknown avg `0.2526` n `1079`
- 1h: commodity avg `0.0597` n `13`; crypto_alt avg `-0.5727` n `235`; crypto_major avg `-0.1075` n `8`; equity avg `-0.0946` n `144`; fx avg `0.0493` n `6`; index avg `-0.0288` n `26`; metal avg `-0.0169` n `20`; unknown avg `-0.1142` n `1077`
- 4h: commodity avg `0.0538` n `13`; crypto_alt avg `-0.695` n `235`; crypto_major avg `-0.0252` n `8`; equity avg `-0.0484` n `144`; fx avg `0.0333` n `6`; index avg `-0.038` n `26`; metal avg `-0.0076` n `20`; unknown avg `-0.1982` n `1047`
- 24h: commodity avg `-0.0872` n `13`; crypto_alt avg `-0.6012` n `235`; crypto_major avg `-0.2205` n `8`; equity avg `-0.1564` n `144`; fx avg `0.0543` n `6`; index avg `0.0482` n `26`; metal avg `-0.0142` n `20`; unknown avg `625.3437` n `800`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
