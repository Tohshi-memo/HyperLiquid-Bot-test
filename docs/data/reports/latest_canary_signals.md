# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T11:52:29.770708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `0.2447` n `234`; crypto_major avg `0.2` n `8`; equity avg `0.0212` n `140`; fx avg `-0.0076` n `6`; index avg `0.0055` n `26`; metal avg `0.005` n `20`; unknown avg `5.8073` n `943`
- 1h: commodity avg `-0.0087` n `12`; crypto_alt avg `0.4711` n `234`; crypto_major avg `0.3199` n `8`; equity avg `0.0283` n `140`; fx avg `0.0066` n `6`; index avg `0.0063` n `26`; metal avg `-0.0059` n `20`; unknown avg `5.1326` n `941`
- 4h: commodity avg `-0.0635` n `12`; crypto_alt avg `-0.0895` n `234`; crypto_major avg `0.1836` n `8`; equity avg `-0.0081` n `140`; fx avg `0.0135` n `6`; index avg `0.011` n `26`; metal avg `0.0004` n `20`; unknown avg `5.263` n `935`
- 24h: commodity avg `0.2406` n `12`; crypto_alt avg `-2.172` n `234`; crypto_major avg `-2.103` n `8`; equity avg `-0.2473` n `140`; fx avg `-0.0414` n `6`; index avg `-0.0384` n `26`; metal avg `-0.0182` n `20`; unknown avg `4.3902` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
