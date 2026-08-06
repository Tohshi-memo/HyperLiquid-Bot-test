# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T06:22:30.344699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.081` n `12`; crypto_alt avg `-0.0257` n `230`; crypto_major avg `-0.1062` n `8`; equity avg `-0.0914` n `108`; fx avg `0.0415` n `6`; index avg `-0.023` n `25`; metal avg `-0.062` n `20`; unknown avg `0.0259` n `782`
- 1h: commodity avg `0.1783` n `12`; crypto_alt avg `-0.0925` n `230`; crypto_major avg `-0.2603` n `8`; equity avg `-0.346` n `108`; fx avg `0.0498` n `6`; index avg `-0.0517` n `25`; metal avg `0.018` n `20`; unknown avg `0.0134` n `750`
- 4h: commodity avg `0.015` n `12`; crypto_alt avg `0.4542` n `230`; crypto_major avg `0.3354` n `8`; equity avg `-0.1836` n `108`; fx avg `0.0621` n `6`; index avg `-0.0409` n `25`; metal avg `-0.2557` n `20`; unknown avg `-0.0029` n `750`
- 24h: commodity avg `0.0603` n `12`; crypto_alt avg `0.0408` n `230`; crypto_major avg `-0.1259` n `8`; equity avg `-2.2196` n `108`; fx avg `0.0131` n `6`; index avg `-0.4099` n `25`; metal avg `0.2119` n `20`; unknown avg `0.8316` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1839`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
