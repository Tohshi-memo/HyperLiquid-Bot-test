# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T04:22:16.488035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0697` n `12`; crypto_alt avg `0.0148` n `228`; crypto_major avg `-0.0151` n `8`; equity avg `0.0489` n `66`; fx avg `0.0061` n `6`; index avg `0.0084` n `23`; metal avg `-0.0851` n `18`; unknown avg `-0.1491` n `384`
- 1h: commodity avg `-0.1372` n `12`; crypto_alt avg `0.1266` n `228`; crypto_major avg `0.0255` n `8`; equity avg `0.2404` n `66`; fx avg `0.0356` n `6`; index avg `0.1387` n `23`; metal avg `0.1077` n `18`; unknown avg `0.085` n `384`
- 4h: commodity avg `-0.1506` n `12`; crypto_alt avg `0.5693` n `228`; crypto_major avg `0.3554` n `8`; equity avg `0.5562` n `66`; fx avg `-0.029` n `6`; index avg `0.1101` n `23`; metal avg `-0.217` n `18`; unknown avg `-0.4102` n `384`
- 24h: commodity avg `0.5637` n `12`; crypto_alt avg `-1.0298` n `228`; crypto_major avg `-0.7627` n `8`; equity avg `0.2429` n `66`; fx avg `-0.1175` n `6`; index avg `-0.4137` n `23`; metal avg `-2.0017` n `18`; unknown avg `0.4815` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0466`, n `668`, weak_sample_signal
