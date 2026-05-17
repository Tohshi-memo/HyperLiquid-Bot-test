# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T18:46:18.713304+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `-0.0711` n `228`; crypto_major avg `-0.0097` n `8`; equity avg `0.0511` n `65`; fx avg `0.0017` n `5`; index avg `0.0027` n `23`; metal avg `-0.0011` n `18`; unknown avg `0.0059` n `384`
- 1h: commodity avg `0.074` n `12`; crypto_alt avg `-0.0212` n `228`; crypto_major avg `0.221` n `8`; equity avg `0.0607` n `65`; fx avg `0.0005` n `5`; index avg `0.0049` n `23`; metal avg `-0.0552` n `18`; unknown avg `-0.0356` n `384`
- 4h: commodity avg `0.1625` n `12`; crypto_alt avg `-0.4652` n `228`; crypto_major avg `0.2429` n `8`; equity avg `0.0677` n `65`; fx avg `0.0112` n `5`; index avg `0.0465` n `23`; metal avg `-0.0195` n `18`; unknown avg `-0.0337` n `384`
- 24h: commodity avg `1.8622` n `12`; crypto_alt avg `-9.6885` n `228`; crypto_major avg `-2.2904` n `8`; equity avg `-2.5546` n `65`; fx avg `-0.1538` n `5`; index avg `-1.5969` n `23`; metal avg `-5.8929` n `18`; unknown avg `550.0252` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
