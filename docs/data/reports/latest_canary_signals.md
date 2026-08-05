# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T01:37:28.784072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `12`; crypto_alt avg `0.0801` n `230`; crypto_major avg `0.0783` n `8`; equity avg `0.0992` n `108`; fx avg `-0.013` n `6`; index avg `0.0049` n `25`; metal avg `0.0119` n `20`; unknown avg `-0.0405` n `781`
- 1h: commodity avg `0.1554` n `12`; crypto_alt avg `0.1489` n `230`; crypto_major avg `0.0337` n `8`; equity avg `-0.42` n `108`; fx avg `-0.0293` n `6`; index avg `-0.0908` n `25`; metal avg `-0.0635` n `20`; unknown avg `-0.0487` n `781`
- 4h: commodity avg `0.2149` n `12`; crypto_alt avg `0.0409` n `230`; crypto_major avg `-0.1156` n `8`; equity avg `0.2867` n `108`; fx avg `-0.0733` n `6`; index avg `0.0175` n `25`; metal avg `-0.02` n `20`; unknown avg `-0.095` n `781`
- 24h: commodity avg `-1.1675` n `12`; crypto_alt avg `0.2067` n `230`; crypto_major avg `0.5241` n `8`; equity avg `3.6677` n `107`; fx avg `0.0817` n `6`; index avg `0.8105` n `25`; metal avg `0.7611` n `20`; unknown avg `0.3421` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
