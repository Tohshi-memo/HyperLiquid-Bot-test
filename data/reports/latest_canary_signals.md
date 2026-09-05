# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T20:22:23.429839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `-0.066` n `232`; crypto_major avg `-0.1413` n `8`; equity avg `-0.0538` n `134`; fx avg `0.0` n `6`; index avg `-0.0208` n `26`; metal avg `0.0002` n `20`; unknown avg `0.2226` n `782`
- 1h: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.1219` n `232`; crypto_major avg `-0.2742` n `8`; equity avg `0.0094` n `134`; fx avg `-0.0145` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0048` n `20`; unknown avg `0.8558` n `780`
- 4h: commodity avg `0.0568` n `12`; crypto_alt avg `0.4118` n `232`; crypto_major avg `0.5564` n `8`; equity avg `0.0465` n `134`; fx avg `-0.0178` n `6`; index avg `0.0316` n `26`; metal avg `0.0201` n `20`; unknown avg `1.1063` n `774`
- 24h: commodity avg `0.1345` n `12`; crypto_alt avg `2.7877` n `232`; crypto_major avg `2.3526` n `8`; equity avg `0.1961` n `134`; fx avg `-0.0328` n `6`; index avg `0.0167` n `26`; metal avg `0.037` n `20`; unknown avg `334.389` n `662`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
