# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T06:22:25.643837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.28` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.0075` n `228`; crypto_major avg `0.0234` n `8`; equity avg `-0.0587` n `72`; fx avg `0.047` n `6`; index avg `-0.0323` n `23`; metal avg `0.0272` n `18`; unknown avg `0.0648` n `420`
- 1h: commodity avg `0.1794` n `12`; crypto_alt avg `0.2233` n `228`; crypto_major avg `0.0936` n `8`; equity avg `0.0295` n `72`; fx avg `0.0607` n `6`; index avg `-0.0907` n `23`; metal avg `-0.2657` n `18`; unknown avg `0.1959` n `410`
- 4h: commodity avg `0.1748` n `12`; crypto_alt avg `1.9808` n `228`; crypto_major avg `1.2155` n `8`; equity avg `0.4522` n `72`; fx avg `0.0962` n `6`; index avg `-0.0745` n `23`; metal avg `-0.1718` n `18`; unknown avg `0.874` n `410`
- 24h: commodity avg `1.1605` n `12`; crypto_alt avg `-1.3297` n `228`; crypto_major avg `-3.6008` n `8`; equity avg `0.9393` n `72`; fx avg `0.0759` n `6`; index avg `1.0744` n `23`; metal avg `-1.4136` n `18`; unknown avg `-0.2332` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
