# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T14:07:36.209391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1547` n `12`; crypto_alt avg `-0.1969` n `230`; crypto_major avg `-0.3968` n `8`; equity avg `-0.3728` n `112`; fx avg `0.0029` n `6`; index avg `-0.0417` n `25`; metal avg `-0.1367` n `20`; unknown avg `0.1754` n `782`
- 1h: commodity avg `0.2902` n `12`; crypto_alt avg `-0.2366` n `230`; crypto_major avg `-0.5197` n `8`; equity avg `-1.2933` n `112`; fx avg `0.0192` n `6`; index avg `-0.1601` n `25`; metal avg `-0.169` n `20`; unknown avg `0.1783` n `782`
- 4h: commodity avg `0.2829` n `12`; crypto_alt avg `-0.2004` n `230`; crypto_major avg `-0.076` n `8`; equity avg `-0.3114` n `112`; fx avg `-0.0277` n `6`; index avg `0.011` n `25`; metal avg `-0.2695` n `20`; unknown avg `-0.0082` n `782`
- 24h: commodity avg `0.508` n `12`; crypto_alt avg `0.0373` n `230`; crypto_major avg `0.3382` n `8`; equity avg `0.8489` n `109`; fx avg `-0.1256` n `6`; index avg `-0.0302` n `25`; metal avg `0.244` n `20`; unknown avg `0.0594` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
